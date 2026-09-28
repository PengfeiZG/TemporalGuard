"""Offline stand-in judge for tests, CI and pipeline dry runs.

CompositionMockJudge is NOT a security model and its numbers are NOT research results. It mimics
the interface and the compositional behaviour of a semantic judge (a directive only becomes
visible when complementary fragments from different categories are combined) so the engine and
the metrics can be exercised end to end without API calls or cost.
"""

from __future__ import annotations

import re
from collections.abc import Sequence

from ..cost import estimate_tokens
from ..models import JudgeResult, ToolOutput, Usage
from .base import Judge
from .prompts import SYSTEM_PROMPT, build_user_message


def _both(verbs: str, objects: str):
    v = re.compile(verbs, re.IGNORECASE)
    o = re.compile(objects, re.IGNORECASE)
    return lambda text: bool(v.search(text) and o.search(text))


_CATEGORIES = {
    "override": _both(
        r"\b(ignore|disregard\w*|supersed\w*|outdated|retired|no longer appl\w*)\b",
        r"\b(instructions?|rules?|guidance|restrictions?|configuration|earlier|previous)\b",
    ),
    "access": _both(
        r"\b(retrieve|read|reading|locate|obtain|requires?)\b",
        r"\b(token|password|credential\w*|secret\w*|api key|environment variables?)\b",
    ),
    "outbound": _both(
        r"\b(send|e-?mail|post|forward|transmit)\b",
        r"[\w.+-]+@[\w-]+\.[\w.]+|https?://\S+|\bendpoint\b",
    ),
}


class CompositionMockJudge(Judge):
    name = "mock"

    @staticmethod
    def categories(text: str) -> set[str]:
        return {name for name, test in _CATEGORIES.items() if test(text)}

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        tagged = {out.index: self.categories(out.content) for out in window}
        own = tagged[window[-1].index]
        union = set().union(*tagged.values())
        prompt_tokens = estimate_tokens(SYSTEM_PROMPT + build_user_message(window, task))
        usage = Usage(input_tokens=prompt_tokens, output_tokens=80, calls=1)

        if own and len(union) >= 2:
            return JudgeResult(
                malicious=True,
                confidence=min(0.95, 0.6 + 0.15 * (len(union) - 1)),
                fragment_indices=sorted(i for i, c in tagged.items() if c),
                reconstructed_instruction=" + ".join(sorted(union)),
                attack_type="data_exfiltration" if "outbound" in union else "instruction_override",
                rationale=f"window combines categories {sorted(union)}",
                usage=usage,
            )
        if own:
            return JudgeResult(
                malicious=False,
                confidence=0.6,
                needs_more_context=True,
                rationale=f"newest output carries {sorted(own)} with no complementary fragment",
                usage=usage,
            )
        return JudgeResult(malicious=False, confidence=0.9, rationale="no directive", usage=usage)
