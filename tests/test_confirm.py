"""Tests for confirm-on-flag: a full-history check after a flag that only adds fragments."""

from temporalguard.config import EngineConfig
from temporalguard.engine import TemporalGuard
from temporalguard.judge.base import Judge, JudgeError
from temporalguard.models import JudgeResult, Usage, Verdict
from temporalguard.schedules import Fibonacci, Fixed
from temporalguard.strategies import STRATEGIES, build_guard


class FlagLastJudge(Judge):
    """Flags whenever the window ends in the marker output; names root fragment if it can see it."""

    def __init__(self, fail_on_full: bool = False, full_size: int | None = None):
        self.calls: list[int] = []
        self.fail_on_full = fail_on_full
        self.full_size = full_size

    def judge(self, window, task=None):
        self.calls.append(len(window))
        if self.fail_on_full and len(window) == self.full_size:
            raise JudgeError("boom")
        if "ATTACK" not in window[-1].content:
            return JudgeResult(False, 0.95, usage=Usage(10, 1, 1))
        frags = [window[-1].index] + [w.index for w in window if "ROOT" in w.content]
        return JudgeResult(True, 0.9, fragment_indices=sorted(set(frags)), usage=Usage(10, 1, 1))


def _run(judge, config=None, schedule=None):
    g = TemporalGuard(judge, schedule=schedule or Fixed(1), gate=False, config=config)
    outs = ["ROOT note"] + [f"filler {i}" for i in range(6)] + ["ATTACK directive"]
    return [g.inspect(o) for o in outs]


def test_confirm_adds_older_fragments_without_changing_the_verdict():
    plain = _run(FlagLastJudge())[-1]
    judge = FlagLastJudge()
    confirmed = _run(judge, EngineConfig(confirm_flags=True))[-1]
    assert plain.verdict == confirmed.verdict == Verdict.QUARANTINE
    assert plain.fragment_indices == [7]
    assert confirmed.fragment_indices == [0, 7]
    assert judge.calls[-2:] == [1, 8]  # small window first, then the whole history
    assert confirmed.windows_examined == [1, 8]
    assert confirmed.usage.calls == 2 and plain.usage.calls == 1


def test_confirm_costs_nothing_when_nothing_is_flagged():
    judge = FlagLastJudge()
    decisions = _run(judge, EngineConfig(confirm_flags=True))
    assert all(d.usage.calls == 1 for d in decisions[:-1])
    assert len(judge.calls) == len(decisions) + 1  # only the flagged output got a second call


def test_confirm_skipped_when_window_already_covers_the_history():
    judge = FlagLastJudge()
    g = TemporalGuard(judge, schedule=Fixed(1), gate=False, config=EngineConfig(confirm_flags=True))
    d = g.inspect("ATTACK directive")  # history of one output: window 1 is already everything
    assert d.verdict.flagged and judge.calls == [1]


def test_failed_confirm_call_keeps_the_original_flag():
    judge = FlagLastJudge(fail_on_full=True, full_size=8)
    d = _run(judge, EngineConfig(confirm_flags=True))[-1]
    assert d.verdict == Verdict.QUARANTINE and d.stage == "judge"
    assert d.fragment_indices == [7] and d.windows_examined == [1]


def test_confirm_strategies_are_registered_and_enable_the_option():
    for name in ("per_message_confirm", "fib_confirm"):
        assert STRATEGIES[name].confirm and not STRATEGIES[name].gate
    g = build_guard("fib_confirm", FlagLastJudge())
    assert g.config.confirm_flags is True and isinstance(g.schedule, Fibonacci)
    assert build_guard("fib", FlagLastJudge()).config.confirm_flags is False


def test_every_schedule_has_fallback_and_confirm_controls():
    grid = {
        "fixed5": ("fixed5_fallback", "fixed5_confirm"),
        "pow2": ("pow2_fallback", "pow2_confirm"),
        "fib": ("fib_fallback", "fib_confirm"),
    }
    for base, (fallback, confirm) in grid.items():
        assert (
            STRATEGIES[fallback].schedule.name.endswith("+fallback")
            or "fallback" in STRATEGIES[fallback].schedule.name
        )
        assert STRATEGIES[confirm].confirm and not STRATEGIES[base].confirm
        assert STRATEGIES[confirm].schedule.name == STRATEGIES[base].schedule.name
    for name in ("fib_fallback_confirm", "pow2_fallback_confirm"):
        assert STRATEGIES[name].confirm and "fallback" in STRATEGIES[name].schedule.name
        assert build_guard(name, FlagLastJudge()).config.confirm_flags


def test_complete_grid_exists_for_every_schedule():
    for base in ("fixed5", "pow2", "fib"):
        for suffix in ("_fallback", "_confirm", "_fallback_confirm"):
            assert f"{base}{suffix}" in STRATEGIES, f"{base}{suffix}"


def test_min3_strategies_skip_small_windows_and_keep_other_settings():
    judge = FlagLastJudge()
    g = build_guard("fib_min3", judge)
    assert g.config.min_window == 3 and not g.config.confirm_flags
    for i in range(8):
        g.inspect(f"filler {i}")
    assert min(judge.calls[2:]) >= 3  # once three outputs exist, no window below 3
    assert STRATEGIES["pow2_min3"].min_window == 3 and STRATEGIES["fib"].min_window == 1
    assert build_guard("fib", judge, config=EngineConfig(min_window=2)).config.min_window == 2
    assert build_guard("fib_min3", judge, config=EngineConfig(min_window=5)).config.min_window == 5


def test_final_candidate_strategies_combine_min_window_fallback_and_confirm():
    for name in ("fib_min3_fallback_confirm", "pow2_min3_fallback_confirm"):
        st = STRATEGIES[name]
        assert st.confirm and st.min_window == 3 and "fallback" in st.schedule.name
        cfg = build_guard(name, FlagLastJudge()).config
        assert cfg.confirm_flags and cfg.min_window == 3
