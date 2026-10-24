"""Two-tier judge: a cheap judge screens everything, a stronger one rules on what it flags.

    cheap judge --(verdict not malicious)--> returned as is, no strong call
         |
         +--(malicious, or unsure if escalate_on="flag_or_unsure")--> strong judge decides

The strong tier sees the same window and task and its verdict REPLACES the cheap one, so the
cascade can lower false alarms (the strong judge says benign) as well as confirm flags. Usage and
dollars are summed over both tiers, using each tier's own price, so cost is comparable with
single-judge runs.

Because the strong tier only runs on flagged windows (about one output in ten in the attack suites
and almost none in benign sessions), it adds little to the cost of a run. `max_strong_calls` is a
hard cap on REAL strong-tier calls (cache hits are free), so a run cannot spend more than intended.
With parallel workers, calls already in flight when the cap is reached may finish, so the cap can
be overshot by at most the number of workers.
"""

from __future__ import annotations

import threading
from collections.abc import Sequence
from dataclasses import replace

from ..cost import PriceTable
from ..models import JudgeResult, ToolOutput, Usage
from .base import BudgetExceeded, Judge
from .cache import CachingJudge


class CascadeJudge(Judge):
    def __init__(
        self,
        cheap: Judge,
        strong: Judge,
        escalate_on: str = "flag",
        cheap_price: PriceTable | None = None,
        strong_price: PriceTable | None = None,
        max_strong_calls: int | None = None,
    ) -> None:
        if escalate_on not in {"flag", "flag_or_unsure"}:
            raise ValueError("escalate_on must be 'flag' or 'flag_or_unsure'")
        self.cheap = cheap
        self.strong = strong
        self.escalate_on = escalate_on
        self.cheap_price = cheap_price
        self.strong_price = strong_price
        self.max_strong_calls = max_strong_calls
        self.name = f"cascade({cheap.name}>{strong.name})"
        self.cheap_calls = 0
        self.escalations = 0
        self._strong_real_calls = 0
        self._lock = threading.Lock()

    # ------------------------------------------------------------------ accounting
    @property
    def strong_real_calls(self) -> int:
        """Strong-tier calls that actually reached the API (cache hits excluded)."""
        if isinstance(self.strong, CachingJudge):
            return self.strong.misses
        return self._strong_real_calls

    def stats(self) -> str:
        return (
            f"cascade: {self.cheap_calls} cheap-tier calls, {self.escalations} escalated, "
            f"{self.strong_real_calls} real strong-tier calls"
        )

    # ------------------------------------------------------------------ judge
    def _escalates(self, r: JudgeResult) -> bool:
        if r.malicious:
            return True
        return self.escalate_on == "flag_or_unsure" and (r.needs_more_context or r.confidence < 0.8)

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        first = self.cheap.judge(window, task)
        with self._lock:
            self.cheap_calls += 1
        if self.cheap_price is not None:
            first.usage.cost_usd = self.cheap_price.cost(first.usage)
        if not self._escalates(first):
            return first
        with self._lock:
            self.escalations += 1
        free = isinstance(self.strong, CachingJudge) and self.strong.is_cached(window, task)
        over = self.max_strong_calls is not None and self.strong_real_calls >= self.max_strong_calls
        if over and not free:
            raise BudgetExceeded(
                f"reached the cap of {self.max_strong_calls} real strong-tier calls; "
                "raise --max-strong-calls and rerun the same command to continue from the cache"
            )
        second = self.strong.judge(window, task)
        with self._lock:
            self._strong_real_calls += 1
        if self.strong_price is not None:
            second.usage.cost_usd = self.strong_price.cost(second.usage)
        total = Usage()
        total.add(first.usage)
        total.add(second.usage)
        return replace(second, usage=total)
