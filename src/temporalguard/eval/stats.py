"""Bootstrap confidence intervals and paired comparisons over episodes.

Episodes are the unit of resampling (a cluster bootstrap), because outputs inside one episode are
not independent. Every statistic is a ratio of sums, so output-level quantities such as the
false-positive rate or tokens per output are weighted correctly.
"""

from __future__ import annotations

import random
from collections.abc import Callable, Sequence

from .metrics import EpisodeResult

# metric name -> function(EpisodeResult) -> (numerator, denominator) or None if not applicable
Contribution = Callable[[EpisodeResult], "tuple[float, float] | None"]


def _recall(r: EpisodeResult) -> tuple[float, float] | None:
    if not r.episode.is_attack:
        return None
    truth = set(r.episode.attack_indices)
    detected = any(d.verdict.flagged and d.output_index in truth for d in r.decisions)
    return (float(detected), 1.0)


def _root(r: EpisodeResult) -> tuple[float, float] | None:
    """1 if the oldest fragment was flagged or named by the judge (see metrics.root_recall)."""
    if not r.episode.is_attack:
        return None
    flagged = [d for d in r.decisions if d.verdict.flagged]
    found = {d.output_index for d in flagged}
    for d in flagged:
        found |= set(d.fragment_indices)
    return (float(min(r.episode.attack_indices) in found), 1.0)


def _fpr(r: EpisodeResult) -> tuple[float, float] | None:
    if r.episode.is_attack:
        return None
    return (float(sum(d.verdict.flagged for d in r.decisions)), float(len(r.decisions)))


def _tokens(r: EpisodeResult) -> tuple[float, float] | None:
    return (float(sum(d.usage.total_tokens for d in r.decisions)), float(len(r.decisions)))


def _calls(r: EpisodeResult) -> tuple[float, float] | None:
    return (float(sum(d.usage.calls for d in r.decisions)), float(len(r.decisions)))


METRICS: dict[str, Contribution] = {
    "recall": _recall,
    "root_recall": _root,
    "fpr_output": _fpr,
    "tokens_per_output": _tokens,
    "judge_calls_per_output": _calls,
}


def _ratio(parts: Sequence[tuple[float, float]]) -> float:
    den = sum(d for _, d in parts)
    return sum(n for n, _ in parts) / den if den else float("nan")


def _percentile(sorted_vals: list[float], q: float) -> float:
    idx = min(len(sorted_vals) - 1, max(0, int(q * len(sorted_vals))))
    return sorted_vals[idx]


def bootstrap_ci(
    results: Sequence[EpisodeResult],
    metric: str,
    n_boot: int = 1000,
    alpha: float = 0.05,
    seed: int = 0,
) -> tuple[float, float, float]:
    """(estimate, lower, upper) percentile bootstrap interval for one metric."""
    contrib = METRICS[metric]
    parts = [c for c in (contrib(r) for r in results) if c is not None]
    if not parts:
        nan = float("nan")
        return nan, nan, nan
    rng = random.Random(seed)
    stats = sorted(_ratio([parts[rng.randrange(len(parts))] for _ in parts]) for _ in range(n_boot))
    return _ratio(parts), _percentile(stats, alpha / 2), _percentile(stats, 1 - alpha / 2)


def paired_difference(
    a: Sequence[EpisodeResult],
    b: Sequence[EpisodeResult],
    metric: str,
    n_boot: int = 1000,
    alpha: float = 0.05,
    seed: int = 0,
) -> tuple[float, float, float]:
    """(a - b, lower, upper): bootstrap interval for the difference between two strategies run
    on the same episodes. If the interval contains 0 the data do not separate them.
    """
    if len(a) != len(b) or any(x.episode.id != y.episode.id for x, y in zip(a, b, strict=True)):
        raise ValueError("paired comparison needs identical episodes in identical order")
    contrib = METRICS[metric]
    pairs = [
        (ca, cb)
        for ca, cb in ((contrib(x), contrib(y)) for x, y in zip(a, b, strict=True))
        if ca is not None and cb is not None
    ]
    if not pairs:
        nan = float("nan")
        return nan, nan, nan
    rng = random.Random(seed)

    def diff(sample: Sequence[tuple[tuple[float, float], tuple[float, float]]]) -> float:
        return _ratio([p[0] for p in sample]) - _ratio([p[1] for p in sample])

    stats = sorted(diff([pairs[rng.randrange(len(pairs))] for _ in pairs]) for _ in range(n_boot))
    return diff(pairs), _percentile(stats, alpha / 2), _percentile(stats, 1 - alpha / 2)
