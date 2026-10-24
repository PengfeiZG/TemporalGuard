"""Run strategies over a suite of episodes."""

from __future__ import annotations

import time
from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor

from ..config import EngineConfig
from ..cost import PriceTable
from ..judge.base import Judge
from ..strategies import STRATEGIES, build_guard, default_strategy_names
from .episodes import Episode, adaptive_suite
from .metrics import (
    EpisodeResult,
    false_alarm_by_family,
    pair_accuracy,
    summarize,
    summarize_by_family,
)
from .stats import bootstrap_ci

CI_METRICS = {
    "recall": "recall_ci",
    "root_recall": "root_ci",
    "fpr_output": "fpr_ci",
    "tokens_per_output": "tokens_ci",
}


def _run_episode(
    name: str, judge: Judge, ep: Episode, config: EngineConfig | None
) -> EpisodeResult:
    guard = build_guard(name, judge, config=config, task=ep.task)
    return EpisodeResult(ep, guard.inspect_all(ep.outputs))


def run_strategy(
    name: str,
    judge: Judge,
    episodes: Sequence[Episode],
    config: EngineConfig | None = None,
    workers: int = 1,
    progress: Callable[[str], None] | None = None,
) -> list[EpisodeResult]:
    """Run one strategy over every episode.

    `workers` > 1 judges several episodes at once. Episodes are independent and each has its own
    guard, so results are identical to a sequential run (the judge verdicts are cached and the
    order of results is preserved); only the wall-clock time and the API request rate change.
    `progress` receives a short status line after every ten episodes.
    """
    if workers < 1:
        raise ValueError("workers must be at least 1")
    start = time.perf_counter()
    results: list[EpisodeResult] = []
    total = len(episodes)

    def note(done: int) -> None:
        if progress and (done % 10 == 0 or done == total):
            progress(f"  {name}: {done}/{total} episodes, {time.perf_counter() - start:.0f}s")

    if workers == 1:
        for i, ep in enumerate(episodes, 1):
            results.append(_run_episode(name, judge, ep, config))
            note(i)
        return results
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for i, result in enumerate(
            pool.map(lambda ep: _run_episode(name, judge, ep, config), episodes), 1
        ):
            results.append(result)
            note(i)
    return results


def run_many(
    judge: Judge,
    episodes: Sequence[Episode],
    strategies: Sequence[str] | None = None,
    config: EngineConfig | None = None,
    workers: int = 1,
    progress: Callable[[str], None] | None = None,
) -> dict[str, list[EpisodeResult]]:
    """Run each strategy once over the same episodes; keep raw results for later analysis."""
    out: dict[str, list[EpisodeResult]] = {}
    for name in strategies or default_strategy_names():
        if progress:
            progress(f"running {name} ...")
        out[name] = run_strategy(name, judge, episodes, config, workers, progress)
    return out


def rows_from_results(
    all_results: dict[str, list[EpisodeResult]],
    price: PriceTable | None = None,
    ci: bool = False,
    n_boot: int = 1000,
    seed: int = 0,
) -> list[dict]:
    rows: list[dict] = []
    for name, results in all_results.items():
        row: dict = {"strategy": name, **summarize(results, price)}
        if ci:
            for metric, key in CI_METRICS.items():
                _, lo, hi = bootstrap_ci(results, metric, n_boot=n_boot, seed=seed)
                row[key] = (lo, hi)
        rows.append(row)
    return rows


def family_rows(all_results: dict[str, list[EpisodeResult]], metric: str = "recall") -> list[dict]:
    """One row per strategy, one column per attack family, for a single metric."""
    rows = []
    for name, results in all_results.items():
        per_family = summarize_by_family(results)
        rows.append({"strategy": name, **{fam: s[metric] for fam, s in per_family.items()}})
    return rows


def benign_family_rows(all_results: dict[str, list[EpisodeResult]]) -> list[dict]:
    """One row per strategy: share of benign sessions with any flag, per benign family."""
    return [
        {"strategy": name, **false_alarm_by_family(results)}
        for name, results in all_results.items()
    ]


def pair_rows(all_results: dict[str, list[EpisodeResult]]) -> list[dict]:
    """One row per strategy: share of attack/twin pairs handled correctly, per family."""
    return [{"strategy": name, **pair_accuracy(results)} for name, results in all_results.items()]


def compare(
    judge: Judge,
    episodes: Sequence[Episode],
    strategies: Sequence[str] | None = None,
    config: EngineConfig | None = None,
    price: PriceTable | None = None,
    ci: bool = False,
    n_boot: int = 1000,
    seed: int = 0,
) -> list[dict]:
    """Run each strategy and return one summary row per strategy."""
    return rows_from_results(run_many(judge, episodes, strategies, config), price, ci, n_boot, seed)


def compare_adaptive(
    judge: Judge,
    strategies: Sequence[str] | None = None,
    config: EngineConfig | None = None,
    seed: int = 0,
    per_set: int = 2,
    workers: int = 1,
    progress: Callable[[str], None] | None = None,
    pool: str = "lexical",
    collect: dict[str, list[EpisodeResult]] | None = None,
) -> list[dict]:
    """Schedule-aware attacker: each strategy faces episodes built around its OWN schedule.

    Reports the attack-side metrics only (there are no benign episodes). A strategy whose
    schedule has no blind spot (`full`, anything with a full fallback) is attacked with a
    fixed-length long-span episode instead, see `adaptive_positions`.
    """
    rows = []
    for name in strategies or default_strategy_names():
        episodes = adaptive_suite(STRATEGIES[name].schedule, seed=seed, per_set=per_set, pool=pool)
        if progress:
            progress(f"running {name} ...")
        results = run_strategy(name, judge, episodes, config, workers, progress)
        if collect is not None:
            collect[name] = results
        rows.append({"strategy": name, **summarize(results)})
    return rows
