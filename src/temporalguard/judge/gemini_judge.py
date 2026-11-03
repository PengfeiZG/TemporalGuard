"""Gemini semantic judge using the official google-genai SDK."""
from __future__ import annotations

import json
import os
import time
from collections.abc import Sequence

from ..models import JudgeResult, ToolOutput, Usage
from .base import Judge, JudgeError, parse_verdict
from .prompts import SYSTEM_PROMPT, build_user_message

DEFAULT_MODEL = "gemini-3.1-flash-lite"


class GeminiJudge(Judge):
    """Gemini judge with JSON output and TemporalGuard's shared verdict validation."""

    name = "gemini"

    def __init__(self, model: str | None = None, client=None, temperature: float = 0.0):
        if client is None:
            try:
                from google import genai
            except ImportError as exc:
                raise ImportError(
                    'GeminiJudge needs google-genai: pip install "temporalguard[gemini]"'
                ) from exc
            client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
        self.client = client
        self.model = model or os.environ.get("TEMPORALGUARD_GEMINI_MODEL", DEFAULT_MODEL)
        self.temperature = temperature

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        if not window:
            raise ValueError("window must not be empty")
        try:
            from google.genai import types
        except ImportError as exc:
            raise ImportError('GeminiJudge needs google-genai') from exc
        start = time.perf_counter()
        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=build_user_message(window, task),
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT +
                    "\nReturn ONLY a JSON object with fields: malicious (boolean), "
                    "confidence (number), needs_more_context (boolean), "
                    "fragment_indices (integer array), reconstructed_instruction (string), "
                    "attack_type (string), rationale (string).",
                    response_mime_type="application/json",
                    temperature=self.temperature,
                ),
            )
        except Exception as exc:
            raise JudgeError(f"Gemini API call failed: {exc}") from exc
        latency = time.perf_counter() - start
        try:
            payload = json.loads(response.text)
            result = parse_verdict(payload, window)
        except (ValueError, TypeError, AttributeError, JudgeError) as exc:
            raise JudgeError(f"Gemini verdict was invalid: {exc}") from exc
        usage = getattr(response, "usage_metadata", None)
        result.usage = Usage(
            int(getattr(usage, "prompt_token_count", 0) or 0),
            int(getattr(usage, "candidates_token_count", 0) or 0) +
            int(getattr(usage, "thoughts_token_count", 0) or 0),
            calls=1,
            latency_s=latency,
        )
        return result
