"""Context-window schedules.

A schedule maps the current history length ``n`` to the ascending list of window sizes the judge
may examine (each window is the most recent ``w`` outputs). The schedule controls only HOW MUCH
context is inspected and in what order, never the security semantics of the verdict.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class WindowSchedule(ABC):
    name: str

    @abstractmethod
    def windows(self, n: int) -> list[int]:
        """Ascending distinct window sizes, each in [1, n], for a history of n outputs."""


class Fibonacci(WindowSchedule):
    """1, 2, 3, 5, 8, 13, ... (terms <= n)."""

    name = "fib"

    def windows(self, n: int) -> list[int]:
        out: list[int] = []
        a, b = 1, 2
        while a <= n:
            out.append(a)
            a, b = b, a + b
        return out


class PowerOfTwo(WindowSchedule):
    """1, 2, 4, 8, 16, ... (terms <= n)."""

    name = "pow2"

    def windows(self, n: int) -> list[int]:
        out: list[int] = []
        w = 1
        while w <= n:
            out.append(w)
            w *= 2
        return out


class Linear(WindowSchedule):
    """1, 1+step, 1+2*step, ... (terms <= n)."""

    def __init__(self, step: int = 4) -> None:
        if step < 1:
            raise ValueError("step must be >= 1")
        self.step = step
        self.name = f"linear{step}"

    def windows(self, n: int) -> list[int]:
        return list(range(1, n + 1, self.step))


class Fixed(WindowSchedule):
    """A single window of k outputs (or the whole history if it is shorter)."""

    def __init__(self, k: int) -> None:
        if k < 1:
            raise ValueError("k must be >= 1")
        self.k = k
        self.name = f"fixed{k}"

    def windows(self, n: int) -> list[int]:
        return [min(self.k, n)] if n > 0 else []


class Full(WindowSchedule):
    """A single window covering the entire history."""

    name = "full"

    def windows(self, n: int) -> list[int]:
        return [n] if n > 0 else []


class WithFullFallback(WindowSchedule):
    """Wrap a schedule and append one final full-history window as a safety net."""

    def __init__(self, inner: WindowSchedule) -> None:
        self.inner = inner
        self.name = f"{inner.name}+fallback"

    def windows(self, n: int) -> list[int]:
        out = self.inner.windows(n)
        if n > 0 and (not out or out[-1] != n):
            out = [*out, n]
        return out


def blind_spot(schedule: WindowSchedule, n: int) -> int:
    """Number of oldest outputs that no window of the schedule ever covers at history length n."""
    windows = schedule.windows(n)
    return n - max(windows) if windows else n


def coverage_stats(schedule: WindowSchedule, n: int) -> dict[str, object]:
    """Worst-case (no early stop) properties of a schedule at history length n."""
    windows = schedule.windows(n)
    blind = blind_spot(schedule, n)
    return {
        "schedule": schedule.name,
        "n": n,
        "windows": windows,
        "steps": len(windows),
        "max_window": max(windows) if windows else 0,
        "blind_spot": blind,
        "worst_case_context": sum(windows),
        "worst_case_vs_full": round(sum(windows) / n, 2) if n else 0.0,
    }
