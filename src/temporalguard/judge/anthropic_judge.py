"""Semantic judge backed by the Claude API (Messages API with forced tool use)."""

from __future__ import annotations

import os
import time
from collections.abc import Sequence

from ..models import JudgeResult, ToolOutput, Usage
from .base import Judge, JudgeError, parse_verdict
from .prompts import SYSTEM_PROMPT, VERDICT_TOOL, build_user_message

DEFAULT_MODEL = "claude-haiku-5-5"


class AnthropicJudge(Judge):
    """Calls Claude once per window and forces a structured `record_verdict` tool call.

    Requires `pip install "temporalguard[anthropic]"` and the ANTHROPIC_API_KEY environment
    variable. Set the model with the `model` argument or TEMPORALGUARD_MODEL.
    """

    name = "anthropic"

    def __init__(
        self,
        model: str | None = None,
        client=None,
        max_tokens: int = 600,
        timeout: float = 60.0,
        max_retries: int = 2,
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
        self.max_tokens = max_tokens

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        start = time.perf_counter()
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                system=SYSTEM_PROMPT,
                tools=[VERDICT_TOOL],
                tool_choice={"type": "tool", "name": VERDICT_TOOL["name"]},
                messages=[{"role": "user", "content": build_user_message(window, task)}],
            )
        except Exception as exc:  # network, auth, rate limit, ...
            raise JudgeError(f"Claude API call failed: {exc}") from exc
        latency = time.perf_counter() - start

        block = next((b for b in response.content if getattr(b, "type", None) == "tool_use"), None)
        if block is None:
            raise JudgeError("response contained no tool_use block")
        result = parse_verdict(block.input, window)
        usage = getattr(response, "usage", None)
        result.usage = Usage(
            input_tokens=int(getattr(usage, "input_tokens", 0) or 0),
            output_tokens=int(getattr(usage, "output_tokens", 0) or 0),
            calls=1,
            latency_s=latency,
        )
        return result
