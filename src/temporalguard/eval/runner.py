"""Run strategies over a suite of episodes."""

from __future__ import annotations

from collections.abc import Sequence

from ..config import EngineConfig
from ..cost import PriceTable
from ..judge.base import Judge
from ..strategies import STRATEGIES, build_guard
from .episodes import Episode
from .metrics import EpisodeResult, summarize


def run_strategy(
    name: str,
    judge: Judge,
    episodes: Sequence[Episode],
    config: EngineConfig | None = None,
) -> list[EpisodeResult]:
    results = []
    for ep in episodes:
        guard = build_guard(name, judge, config=config, task=ep.task)
        results.append(EpisodeResult(ep, guard.inspect_all(ep.outputs)))
    return results


def compare(
    judge: Judge,
    episodes: Sequence[Episode],
    strategies: Sequence[str] | None = None,
    config: EngineConfig | None = None,
    price: PriceTable | None = None,
) -> list[dict[str, float | str]]:
    """Run each strategy and return one summary row per strategy."""
    rows: list[dict[str, float | str]] = []
    for name in strategies or list(STRATEGIES):
        summary = summarize(run_strategy(name, judge, episodes, config), price)
        rows.append({"strategy": name, **summary})
    return rows
