"""Semantic judges: the LLM component that reasons over a window of tool outputs."""

from .base import Judge, JudgeError, parse_verdict
from .mock import CompositionMockJudge

__all__ = ["CompositionMockJudge", "Judge", "JudgeError", "parse_verdict"]


def __getattr__(name: str):  # lazy import so the `anthropic` package stays optional
    if name == "AnthropicJudge":
        from .anthropic_judge import AnthropicJudge

        return AnthropicJudge
    raise AttributeError(name)
