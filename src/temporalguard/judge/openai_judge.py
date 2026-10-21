"""Semantic judge backed by the OpenAI API (Chat Completions with a forced function call)."""

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


class OpenAIJudge(Judge):
    """Calls OpenAI once per window and forces a structured `record_verdict` function call.

    Requires `pip install "temporalguard[openai]"` and the OPENAI_API_KEY environment variable.
    Set the model with the `model` argument or TEMPORALGUARD_OPENAI_MODEL.

    Some models reject function tools on Chat Completions unless reasoning is turned off
    (error: "Function tools with reasoning_effort are not supported ... set reasoning_effort to
    'none'"). Pass `reasoning_effort="none"` or set TEMPORALGUARD_OPENAI_REASONING_EFFORT=none.
    It is only sent when set, because models without reasoning reject the parameter.
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

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
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
        try:
            payload = json.loads(call.function.arguments)
        except (TypeError, ValueError) as exc:
            raise JudgeError(f"verdict arguments were not valid JSON: {exc}") from exc
        if not isinstance(payload, dict):
            raise JudgeError("verdict arguments were not a JSON object")

        result = parse_verdict(payload, window)
        usage = getattr(response, "usage", None)
        result.usage = Usage(
            input_tokens=int(getattr(usage, "prompt_tokens", 0) or 0),
            output_tokens=int(getattr(usage, "completion_tokens", 0) or 0),
            calls=1,
            latency_s=latency,
        )
        return result
