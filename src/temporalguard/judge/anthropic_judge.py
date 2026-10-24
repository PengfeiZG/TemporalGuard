"""Semantic judge backed by the Claude API (Messages API, structured verdict via a tool call)."""

from __future__ import annotations

import os
import time
from collections.abc import Sequence

from ..models import JudgeResult, ToolOutput, Usage
from .base import Judge, JudgeError, parse_verdict
from .prompts import SYSTEM_PROMPT, VERDICT_TOOL, build_user_message

DEFAULT_MODEL = "claude-haiku-5-5"
DEFAULT_MAX_TOKENS = 600

# Models that reject tool_choice "any" / "tool" with a 400 ("type 'tool' and 'any' are not supported
# for this model"). For them the judge sends tool_choice "auto" and asks for the tool in the prompt.
NO_FORCED_TOOL_PREFIXES = ("claude-sonnet-5-5", "claude-opus-5", "claude-fable", "claude-mythos")
AUTO_TOOL_SUFFIX = (
    "\n\nAnswer only by calling the record_verdict tool. Do not write any other text."
)
FOLLOW_UP = (
    "Do not answer in text. Record your verdict now by calling the record_verdict tool, "
    "using the analysis above."
)


def supports_forced_tool_use(model: str) -> bool:
    return not model.startswith(NO_FORCED_TOOL_PREFIXES)


class AnthropicJudge(Judge):
    """Calls Claude once per window and gets a structured `record_verdict` tool call.

    Requires `pip install "temporalguard[anthropic]"` and the ANTHROPIC_API_KEY environment
    variable. Set the model with the `model` argument or TEMPORALGUARD_MODEL.

    Haiku 5.5 accepts a forced tool call (`tool_choice` type "tool"). Sonnet 5.5, Opus 5.x and
    the Fable and Mythos models do not, so for them the judge sends `tool_choice` "auto" and
    ends the system prompt with an instruction to call the tool. Sonnet 5.5 also thinks before
    answering by default (billed as output tokens), so it is sent `thinking` "between_tools",
    the lowest setting it allows. Override the choice with `tool_choice="forced"|"auto"` or
    TEMPORALGUARD_ANTHROPIC_TOOL_CHOICE.

    With `auto` the model sometimes answers in plain text instead of calling the tool, and for
    some windows it does so every time. The judge then continues the conversation: it passes the
    model's own text back and asks it to record the verdict with the tool (up to `tool_retries`
    times). The tokens of every attempt are counted in the usage so cost stays honest. Forced
    calls are never retried.
    """

    name = "anthropic"

    def __init__(
        self,
        model: str | None = None,
        client=None,
        max_tokens: int | None = None,
        timeout: float = 60.0,
        max_retries: int = 2,
        tool_choice: str | None = None,
        tool_retries: int = 2,
    ) -> None:
        if client is None:
            try:
                import anthropic
            except ImportError as exc:  # pragma: no cover - depends on environment
                raise ImportError(
                    "AnthropicJudge needs the anthropic package: "
                    'pip install "temporalguard[anthropic]"'
                ) from exc
            client = anthropic.Anthropic(timeout=timeout, max_retries=max_retries)
        self.client = client
        self.model = model or os.environ.get("TEMPORALGUARD_MODEL", DEFAULT_MODEL)
        self._max_tokens = max_tokens
        mode = tool_choice or os.environ.get("TEMPORALGUARD_ANTHROPIC_TOOL_CHOICE")
        if mode is None:
            mode = "forced" if supports_forced_tool_use(self.model) else "auto"
        if mode not in {"forced", "auto"}:
            raise ValueError("tool_choice must be 'forced' or 'auto'")
        self.tool_choice_mode = mode
        # Thinking tokens count against max_tokens. The "auto" models think a little before the
        # tool call, so they get a larger budget (unused tokens are not billed).
        self.max_tokens = self._max_tokens or (2000 if mode == "auto" else DEFAULT_MAX_TOKENS)
        self.tool_retries = max(0, tool_retries)

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        start = time.perf_counter()
        request: dict = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "system": SYSTEM_PROMPT,
            "tools": [VERDICT_TOOL],
            "tool_choice": {"type": "tool", "name": VERDICT_TOOL["name"]},
            "messages": [{"role": "user", "content": build_user_message(window, task)}],
        }
        if self.tool_choice_mode == "auto":
            request["tool_choice"] = {"type": "auto"}
            request["system"] = SYSTEM_PROMPT + AUTO_TOOL_SUFFIX
            if self.model.startswith("claude-sonnet-5-5"):
                request["thinking"] = {"type": "between_tools"}
        attempts = 1 + (self.tool_retries if self.tool_choice_mode == "auto" else 0)
        in_tok = out_tok = used = 0
        block = None
        last_text = ""
        stop_reason = None
        while used < attempts and block is None:
            used += 1
            try:
                response = self.client.messages.create(**request)
            except Exception as exc:  # network, auth, rate limit, ...
                raise JudgeError(f"Claude API call failed: {exc}") from exc
            usage = getattr(response, "usage", None)
            in_tok += int(getattr(usage, "input_tokens", 0) or 0)
            out_tok += int(getattr(usage, "output_tokens", 0) or 0)
            blocks = list(response.content)
            stop_reason = getattr(response, "stop_reason", None)
            block = next((b for b in blocks if getattr(b, "type", None) == "tool_use"), None)
            if block is None:
                last_text = " ".join(
                    getattr(b, "text", "") for b in blocks if getattr(b, "type", None) == "text"
                ).strip()
                # continue the conversation: show the model its own answer and ask for the tool call
                request = {
                    **request,
                    "messages": [
                        request["messages"][0],
                        {"role": "assistant", "content": last_text or "(no text)"},
                        {"role": "user", "content": FOLLOW_UP},
                    ],
                }
        if block is None:
            plural = "s" if used > 1 else ""
            snippet = last_text.replace("\n", " ")[:160]
            raise JudgeError(
                f"response contained no tool_use block (after {used} attempt{plural}, "
                f"stop_reason={stop_reason}); last text: {snippet!r}"
            )
        result = parse_verdict(block.input, window)
        result.usage = Usage(
            input_tokens=in_tok,
            output_tokens=out_tok,
            calls=used,
            latency_s=time.perf_counter() - start,
        )
        return result
