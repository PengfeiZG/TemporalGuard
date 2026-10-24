"""Gate calibration without any API calls.

For a scorer (the semantic scanner's best similarity, or the keyword scanner's risk), collect the
score of every output in a set of families and split them into three populations:

- fragments: the true fragments of attacks (what the gate must let through to the judge),
- twins:     the fragments of the harmless benign twins (hard negatives),
- benign:    everything else (ordinary filler and benign sessions; each one escalated is a wasted
             judge call).

`escalated_at(cutoff)` is the share of each population a gate with that cutoff would send to the
judge. A good gate escalates nearly all fragments and few benign outputs.
"""

from __future__ import annotations

import random
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field

from ..models import ToolOutput
from .episodes import Episode, build_suite

ScoreFn = Callable[[ToolOutput, Sequence[ToolOutput]], float]


@dataclass
class GatePopulation:
    fragments: list[float] = field(default_factory=list)
    twins: list[float] = field(default_factory=list)
    benign: list[float] = field(default_factory=list)

    def escalated_at(self, cutoff: float) -> dict[str, float]:
        def share(xs: list[float]) -> float:
            return sum(x >= cutoff for x in xs) / len(xs) if xs else float("nan")

        return {
            "fragments": share(self.fragments),
            "twins": share(self.twins),
            "benign": share(self.benign),
        }


def scores_of(episode: Episode, score_fn: ScoreFn) -> list[float]:
    outputs = [ToolOutput(i, tool, text) for i, (tool, text) in enumerate(episode.outputs)]
    return [score_fn(o, outputs[:i]) for i, o in enumerate(outputs)]


def collect(
    families: Sequence[str],
    score_fn: ScoreFn,
    seed: int = 0,
    per_family: int = 12,
    benign_sessions: int = 20,
) -> GatePopulation:
    """Score every output of `families` (built one family at a time) plus plain benign sessions."""
    pop = GatePopulation()
    rng = random.Random(seed)
    episodes: list[Episode] = []
    for fam in families:
        size = 27 if fam.startswith("agentdojo") and not fam.endswith("_benign") else per_family
        if fam == "agentdojo_benign":
            size = 40
        episodes += build_suite(rng.randint(0, 10**6), size, 0, [fam])
    episodes += build_suite(rng.randint(0, 10**6), 0, benign_sessions, ["adjacent"])
    for ep in episodes:
        truth = set(ep.attack_indices)
        is_twin = ep.family.endswith("_twin")
        twin_positions = _twin_positions(ep, episodes) if is_twin else set()
        for i, score in enumerate(scores_of(ep, score_fn)):
            if i in truth:
                pop.fragments.append(score)
            elif i in twin_positions:
                pop.twins.append(score)
            elif not (ep.is_attack and i in truth):
                pop.benign.append(score)
    return pop


def _twin_positions(twin: Episode, episodes: Sequence[Episode]) -> set[int]:
    """Indices where a twin differs from its attack episode (its harmless fragments)."""
    base_id = twin.id.replace(twin.family, twin.family.removesuffix("_twin"), 1)
    for ep in episodes:
        if ep.id == base_id and len(ep.outputs) == len(twin.outputs):
            return set(ep.attack_indices)
    return set()
