"""Named detection strategies used by the experiments.

Each strategy is a (window schedule, gate on/off) pair. Comparing them isolates two separate
factors: how much context is inspected (the schedule) and whether a cheap gate skips the LLM.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

from .config import EngineConfig
from .engine import TemporalGuard
from .judge.base import Judge
from .scanner.heuristic import HeuristicScanner, Scanner
from .scanner.stateful import StatefulScanner
from .schedules import (
    Fibonacci,
    Fixed,
    Full,
    PowerOfTwo,
    WindowSchedule,
    WithFullFallback,
)


@dataclass(frozen=True)
class Strategy:
    name: str
    schedule: WindowSchedule
    gate: bool
    description: str
    scanner: str = "heuristic"  # "heuristic" or "stateful"
    confirm: bool = False  # EngineConfig.confirm_flags: full-history check after a flag
    min_window: int = 1  # skip schedule windows smaller than this (early-stop ablation)


STRATEGIES: dict[str, Strategy] = {
    s.name: s
    for s in (
        Strategy("per_message", Fixed(1), False, "A: judge each output alone"),
        Strategy("fixed5", Fixed(5), False, "B: judge the last 5 outputs"),
        Strategy("full", Full(), False, "C: judge the whole history every time"),
        Strategy("pow2", PowerOfTwo(), False, "D: escalate 1,2,4,8,16"),
        Strategy("fib", Fibonacci(), False, "E: escalate 1,2,3,5,8,13"),
        Strategy("gated_full", Full(), True, "F: cheap gate, then one full-history judge"),
        Strategy("pow2_gated", PowerOfTwo(), True, "D + cheap gate"),
        Strategy("fib_gated", Fibonacci(), True, "E + cheap gate"),
        Strategy(
            "per_message_confirm",
            Fixed(1),
            False,
            "A + full-history check on flags",
            "heuristic",
            True,
        ),
        Strategy(
            "fib_confirm", Fibonacci(), False, "E + full-history check on flags", "heuristic", True
        ),
        # Early-stop ablation: never start below a window of 3, so a judge that is confident about
        # a lone fragment cannot end escalation before seeing any context.
        Strategy("fib_min3", Fibonacci(), False, "E, first window >= 3", "heuristic", False, 3),
        Strategy("pow2_min3", PowerOfTwo(), False, "D, first window >= 3", "heuristic", False, 3),
        # Candidate final designs: skip lone-output windows, end with a full window, check flags.
        Strategy(
            "fib_min3_fallback_confirm",
            WithFullFallback(Fibonacci()),
            False,
            "E from window 3 + final full window + check on flags",
            "heuristic",
            True,
            3,
        ),
        Strategy(
            "pow2_min3_fallback_confirm",
            WithFullFallback(PowerOfTwo()),
            False,
            "D from window 3 + final full window + check on flags",
            "heuristic",
            True,
            3,
        ),
        Strategy("fib_fallback", WithFullFallback(Fibonacci()), False, "E + final full window"),
        # Controls so that any gain from a full-history safeguard is not credited to Fibonacci.
        Strategy(
            "fixed5_fallback", WithFullFallback(Fixed(5)), False, "fixed-5 + final full window"
        ),
        Strategy("pow2_fallback", WithFullFallback(PowerOfTwo()), False, "D + final full window"),
        Strategy(
            "fixed5_confirm",
            Fixed(5),
            False,
            "fixed-5 + full-history check on flags",
            "heuristic",
            True,
        ),
        Strategy(
            "pow2_confirm",
            PowerOfTwo(),
            False,
            "D + full-history check on flags",
            "heuristic",
            True,
        ),
        Strategy(
            "fib_fallback_confirm",
            WithFullFallback(Fibonacci()),
            False,
            "E + final full window + check on flags",
            "heuristic",
            True,
        ),
        Strategy(
            "fixed5_fallback_confirm",
            WithFullFallback(Fixed(5)),
            False,
            "fixed-5 + final full window + check on flags",
            "heuristic",
            True,
        ),
        Strategy(
            "pow2_fallback_confirm",
            WithFullFallback(PowerOfTwo()),
            False,
            "D + final full window + check on flags",
            "heuristic",
            True,
        ),
        Strategy("fib_stateful", Fibonacci(), True, "E + history-aware gate", "stateful"),
        Strategy("pow2_stateful", PowerOfTwo(), True, "D + history-aware gate", "stateful"),
        Strategy("gated_full_stateful", Full(), True, "F with a history-aware gate", "stateful"),
    )
}


def make_scanner(kind: str) -> Scanner:
    if kind == "heuristic":
        return HeuristicScanner()
    if kind == "stateful":
        return StatefulScanner()
    raise KeyError(f"unknown scanner kind {kind!r}")


def build_guard(
    name: str,
    judge: Judge,
    scanner: Scanner | None = None,
    config: EngineConfig | None = None,
    task: str | None = None,
) -> TemporalGuard:
    if name not in STRATEGIES:
        raise KeyError(f"unknown strategy {name!r}; choose from {sorted(STRATEGIES)}")
    strategy = STRATEGIES[name]
    if strategy.confirm:
        config = replace(config or EngineConfig(), confirm_flags=True)
    if strategy.min_window > 1:
        base = config or EngineConfig()
        config = replace(base, min_window=max(base.min_window, strategy.min_window))
    return TemporalGuard(
        judge=judge,
        scanner=scanner or (make_scanner(strategy.scanner) if strategy.gate else None),
        schedule=strategy.schedule,
        config=config,
        gate=strategy.gate,
        task=task,
    )
