"""History-aware gate.

The plain HeuristicScanner only reads the newest output, so a fragment that is harmless on its own
(for example "Locate the API key") never reaches the judge. StatefulScanner keeps the gate cheap
(still regex only, no LLM) but lets it notice that the newest output adds a *different attack
stage* to stages already seen in recent outputs: override -> access -> outbound. When that
happens the output is escalated to the judge even if its own lexical score is low.

This targets the gate-miss weakness. It costs extra judge calls on benign sessions that happen to
mention several stages, which the evaluation reports as extra tokens and false escalations.
"""

from __future__ import annotations

from collections.abc import Sequence

from ..models import ToolOutput
from .heuristic import HeuristicScanner, Scanner

# attack stage -> HeuristicScanner feature names that signal it
DEFAULT_STAGES: dict[str, tuple[str, ...]] = {
    "override": ("override",),
    "access": ("sensitive_data",),
    "outbound": ("destination", "outbound_verb"),
}


class StatefulScanner(Scanner):
    """Boosts an output's risk when it completes a multi-stage pattern with recent history.

    lookback:   how many earlier outputs count as "recent".
    min_stages: distinct stages (current output plus lookback) needed to trigger the boost.
    boost:      risk floor applied when triggered; keep it >= the engine's gate_threshold.
    """

    def __init__(
        self,
        base: HeuristicScanner | None = None,
        stages: dict[str, tuple[str, ...]] | None = None,
        lookback: int = 30,
        min_stages: int = 2,
        boost: float = 0.5,
    ) -> None:
        if lookback < 1 or min_stages < 2 or not 0.0 <= boost <= 1.0:
            raise ValueError("lookback >= 1, min_stages >= 2 and boost in [0, 1] are required")
        self.base = base or HeuristicScanner()
        self.stages = stages or DEFAULT_STAGES
        self.lookback = lookback
        self.min_stages = min_stages
        self.boost = boost
        self._cache: dict[str, frozenset[str]] = {}

    def stages_of(self, text: str) -> frozenset[str]:
        cached = self._cache.get(text)
        if cached is None:
            matched = set(self.base.matched(text))
            cached = frozenset(s for s, feats in self.stages.items() if matched & set(feats))
            self._cache[text] = cached
        return cached

    def score(self, output: ToolOutput, history: Sequence[ToolOutput] = ()) -> float:
        own = self.base.score(output)
        current = self.stages_of(output.content)
        if not current:
            return own
        earlier: set[str] = set()
        for prev in history[-self.lookback :]:
            earlier |= self.stages_of(prev.content)
        # the history must contribute a stage the newest output does not already carry
        if earlier - current and len(current | earlier) >= self.min_stages:
            return max(own, self.boost)
        return own
