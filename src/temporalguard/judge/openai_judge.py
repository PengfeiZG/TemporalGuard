"""Semantic judge backed by the OpenAI API (forced function call; Chat Completions or Responses)."""

from __future__ import annotations

import json
import os
import time
from collections.abc import Sequence

from ..models import JudgeResult, ToolOutput, Usage
from .base import Judge, JudgeError, parse_verdict
from .prompts import SYSTEM_PROMPT, VERDICT_TOOL, build_user_message

# Best guess at a cheap current model. Override with the `model` argument, the --model CLI flag,
# or the TEMPORALGUARD_OPENAI_MODEL environment variable.
DEFAULT_MODEL = "gpt-6-luna"


def _tool_spec() -> dict:
    return {
        "type": "function",
        "function": {
            "name": VERDICT_TOOL["name"],
            "description": VERDICT_TOOL["description"],
            "parameters": VERDICT_TOOL["input_schema"],
        },
    }


def _responses_tool_spec() -> dict:
    """The Responses API takes function tools flat, without the Chat Completions `function` key."""
    return {
        "type": "function",
        "name": VERDICT_TOOL["name"],
        "description": VERDICT_TOOL["description"],
        "parameters": VERDICT_TOOL["input_schema"],
    }


class OpenAIJudge(Judge):
    """Calls OpenAI once per window and forces a structured `record_verdict` function call.

    Requires `pip install "temporalguard[openai]"` and the OPENAI_API_KEY environment variable.
    Set the model with the `model` argument or TEMPORALGUARD_OPENAI_MODEL.

    Some models reject function tools on Chat Completions unless reasoning is turned off
    (error: "Function tools with reasoning_effort are not supported ... set reasoning_effort to
    'none'"). Pass `reasoning_effort="none"` or set TEMPORALGUARD_OPENAI_REASONING_EFFORT=none.
    It is only sent when set, because models without reasoning reject the parameter.

    Models that do not support `none` (for example GPT-6.1 Sol and GPT-6 Astra) cannot do function
    calls on Chat Completions at all. For them set a real effort (`low`) and the judge uses the
    Responses API instead. `api` forces a path: "chat", "responses", or "auto" (the default: the
    Responses API whenever a reasoning effort other than `none` is set). Reasoning tokens count as
    output tokens and are billed as such, so keep the effort low and `max_output_tokens` modest.
    """

    name = "openai"

    def __init__(
        self,
        model: str | None = None,
        client=None,
        max_completion_tokens: int = 600,
        timeout: float = 60.0,
        max_retries: int = 2,
        reasoning_effort: str | None = None,
        api: str | None = None,
        max_output_tokens: int = 2000,
    ) -> None:
        if client is None:
            try:
                import openai
            except ImportError as exc:  # pragma: no cover - depends on environment
                raise ImportError(
                    'OpenAIJudge needs the openai package: pip install "temporalguard[openai]"'
                ) from exc
            client = openai.OpenAI(timeout=timeout, max_retries=max_retries)
        self.client = client
        self.model = model or os.environ.get("TEMPORALGUARD_OPENAI_MODEL", DEFAULT_MODEL)
        self.max_completion_tokens = max_completion_tokens
        self.reasoning_effort = reasoning_effort or os.environ.get(
            "TEMPORALGUARD_OPENAI_REASONING_EFFORT"
        )
        self.api = api or os.environ.get("TEMPORALGUARD_OPENAI_API", "auto")
        if self.api not in {"auto", "chat", "responses"}:
            raise ValueError("api must be 'auto', 'chat' or 'responses'")
        self.max_output_tokens = max_output_tokens

    def uses_responses(self) -> bool:
        if self.api != "auto":
            return self.api == "responses"
        return self.reasoning_effort not in (None, "", "none")

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        if self.uses_responses():
            return self._judge_responses(window, task)
        return self._judge_chat(window, task)

    def _judge_responses(self, window: Sequence[ToolOutput], task: str | None) -> JudgeResult:
        start = time.perf_counter()
        extra = {"reasoning": {"effort": self.reasoning_effort}} if self.reasoning_effort else {}
        try:
            response = self.client.responses.create(
                model=self.model,
                max_output_tokens=self.max_output_tokens,
                input=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": build_user_message(window, task)},
                ],
                tools=[_responses_tool_spec()],
                tool_choice={"type": "function", "name": VERDICT_TOOL["name"]},
                **extra,
            )
        except Exception as exc:  # network, auth, rate limit, unsupported parameter, ...
            raise JudgeError(f"OpenAI API call failed: {exc}") from exc
        latency = time.perf_counter() - start
        try:
            call = next(
                (
                    item
                    for item in response.output
                    if getattr(item, "type", None) == "function_call"
                    and getattr(item, "name", None) == VERDICT_TOOL["name"]
                ),
                None,
            )
        except (AttributeError, TypeError) as exc:
            raise JudgeError(f"unexpected response shape: {exc}") from exc
        if call is None:
            raise JudgeError("response contained no record_verdict call (output may be truncated)")
        usage = getattr(response, "usage", None)
        return self._finish(
            call.arguments,
            window,
            int(getattr(usage, "input_tokens", 0) or 0),
            int(getattr(usage, "output_tokens", 0) or 0),
            latency,
        )

    def _finish(self, arguments, window, in_tok: int, out_tok: int, latency: float) -> JudgeResult:
        try:
            payload = json.loads(arguments)
        except (TypeError, ValueError) as exc:
            raise JudgeError(f"verdict arguments were not valid JSON: {exc}") from exc
        if not isinstance(payload, dict):
            raise JudgeError("verdict arguments were not a JSON object")
        result = parse_verdict(payload, window)
        result.usage = Usage(in_tok, out_tok, calls=1, latency_s=latency)
        return result

    def _judge_chat(self, window: Sequence[ToolOutput], task: str | None) -> JudgeResult:
        start = time.perf_counter()
        extra = {"reasoning_effort": self.reasoning_effort} if self.reasoning_effort else {}
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_completion_tokens=self.max_completion_tokens,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": build_user_message(window, task)},
                ],
                tools=[_tool_spec()],
                tool_choice={"type": "function", "function": {"name": VERDICT_TOOL["name"]}},
                **extra,
            )
        except Exception as exc:  # network, auth, rate limit, unsupported parameter, ...
            raise JudgeError(f"OpenAI API call failed: {exc}") from exc
        latency = time.perf_counter() - start

        try:
            message = response.choices[0].message
            calls = message.tool_calls or []
            call = next(
                (c for c in calls if getattr(c.function, "name", None) == VERDICT_TOOL["name"]),
                None,
            )
        except (AttributeError, IndexError, TypeError) as exc:
            raise JudgeError(f"unexpected response shape: {exc}") from exc
        if call is None:
            raise JudgeError("response contained no record_verdict call")
        usage = getattr(response, "usage", None)
        return self._finish(
            call.function.arguments,
            window,
            int(getattr(usage, "prompt_tokens", 0) or 0),
            int(getattr(usage, "completion_tokens", 0) or 0),
            latency,
        )
