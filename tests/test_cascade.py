"""Tests for the two-tier cascade judge, dollar accounting and the call cap."""

import pytest

from temporalguard.cli import main
from temporalguard.cost import PriceTable
from temporalguard.eval import build_suite, run_many, summarize
from temporalguard.judge import BudgetExceeded, CachingJudge, CascadeJudge, CompositionMockJudge
from temporalguard.judge.base import Judge
from temporalguard.models import JudgeResult, ToolOutput, Usage

W = [ToolOutput(0, "t", "a"), ToolOutput(1, "t", "b")]


class Scripted(Judge):
    """Returns a fixed verdict and counts calls; usage is 1000 in / 100 out per call."""

    def __init__(self, name, malicious, confidence=0.95, needs_more=False):
        self.name = name
        self.malicious, self.confidence, self.needs_more = malicious, confidence, needs_more
        self.calls = 0

    def judge(self, window, task=None):
        self.calls += 1
        return JudgeResult(
            self.malicious,
            self.confidence,
            needs_more_context=self.needs_more,
            fragment_indices=[window[-1].index] if self.malicious else [],
            rationale=self.name,
            usage=Usage(1000, 100, 1),
        )


CHEAP_P, STRONG_P = PriceTable(0.1, 0.5), PriceTable(2.0, 10.0)


def test_benign_cheap_verdict_never_reaches_the_strong_tier():
    cheap, strong = Scripted("cheap", False), Scripted("strong", True)
    c = CascadeJudge(cheap, strong, cheap_price=CHEAP_P, strong_price=STRONG_P)
    r = c.judge(W)
    assert not r.malicious and strong.calls == 0 and c.escalations == 0
    assert r.usage.calls == 1 and r.usage.cost_usd == pytest.approx(CHEAP_P.cost(r.usage))


def test_flag_escalates_and_the_strong_verdict_replaces_the_cheap_one():
    cheap, strong = Scripted("cheap", True), Scripted("strong", False)
    c = CascadeJudge(cheap, strong, cheap_price=CHEAP_P, strong_price=STRONG_P)
    r = c.judge(W)
    assert not r.malicious and r.rationale == "strong"  # strong tier overrules the flag
    assert r.usage.calls == 2 and r.usage.input_tokens == 2000
    expected = CHEAP_P.cost(Usage(1000, 100)) + STRONG_P.cost(Usage(1000, 100))
    assert r.usage.cost_usd == pytest.approx(expected)
    assert c.escalations == 1 and c.cheap_calls == 1 and c.strong_real_calls == 1


def test_confirmed_flag_keeps_strong_fragments():
    c = CascadeJudge(Scripted("cheap", True), Scripted("strong", True))
    r = c.judge(W)
    assert r.malicious and r.fragment_indices == [1]


def test_flag_or_unsure_also_escalates_unsure_benign_verdicts():
    unsure = Scripted("cheap", False, confidence=0.5)
    c = CascadeJudge(unsure, Scripted("strong", True), escalate_on="flag_or_unsure")
    assert c.judge(W).malicious
    needs = Scripted("cheap", False, needs_more=True)
    assert (
        CascadeJudge(needs, Scripted("strong", True), escalate_on="flag_or_unsure")
        .judge(W)
        .malicious
    )
    assert not CascadeJudge(unsure, Scripted("strong", True), escalate_on="flag").judge(W).malicious
    with pytest.raises(ValueError):
        CascadeJudge(unsure, unsure, escalate_on="always")


def test_call_cap_stops_before_the_call_that_would_exceed_it():
    strong = Scripted("strong", True)
    c = CascadeJudge(Scripted("cheap", True), strong, max_strong_calls=2)
    c.judge(W)
    c.judge(W)
    with pytest.raises(BudgetExceeded):
        c.judge(W)
    assert strong.calls == 2  # the third call never reached the API


def test_cache_hits_do_not_count_against_the_cap(tmp_path):
    strong = Scripted("strong", True)
    cached = CachingJudge(strong, tmp_path / "s.jsonl")
    c = CascadeJudge(Scripted("cheap", True), cached, max_strong_calls=1)
    for _ in range(5):  # same window: one real call, four cache hits
        c.judge(W)
    assert strong.calls == 1 and cached.hits == 4 and c.strong_real_calls == 1


def test_cost_usd_round_trips_through_the_cache(tmp_path):
    inner = Scripted("s", True)
    cj = CachingJudge(inner, tmp_path / "c.jsonl")
    r = CascadeJudge(Scripted("c", False), cj, escalate_on="flag_or_unsure")  # not escalated
    assert r.judge(W).usage.cost_usd == 0.0  # no price given: stays zero
    first = Usage(5, 1, 1, 0.1, 0.25)
    assert Usage.__dataclass_fields__["cost_usd"] and first.cost_usd == 0.25
    old_entry = {"input_tokens": 1, "output_tokens": 1, "calls": 1, "latency_s": 0.0}
    assert Usage(**old_entry).cost_usd == 0.0  # caches written before this field still load


def test_summarize_reports_dollars_from_a_priced_cascade():
    judge = CascadeJudge(
        CompositionMockJudge(), CompositionMockJudge(), cheap_price=CHEAP_P, strong_price=STRONG_P
    )
    suite = build_suite(seed=0, per_family=1, benign=1, families=["adjacent"])
    results = run_many(judge, suite, ["full"])["full"]
    n_out = sum(len(r.decisions) for r in results)
    s = summarize(results)
    assert s["cost_usd_total"] > 0
    assert s["usd_per_output"] == pytest.approx(s["cost_usd_total"] / n_out)


def test_cli_cascade_runs_end_to_end_with_mock_tiers_and_reports_stats(capsys):
    argv = ["eval", "--judge", "cascade", "--cheap", "mock", "--strong", "mock",
            "--cheap-price", "0.1", "0.5", "--strong-price", "2", "10",
            "--families", "adjacent", "--per-family", "2", "--benign", "1",
            "--strategies", "per_message", "full", "--max-strong-calls", "500"]  # fmt: skip
    assert main(argv) == 0
    captured = capsys.readouterr()
    assert "$/out" in captured.out and "cascade:" in captured.err


def test_cli_cascade_stops_cleanly_when_the_cap_is_hit(capsys):
    argv = ["eval", "--judge", "cascade", "--cheap", "mock", "--strong", "mock",
            "--families", "adjacent", "--per-family", "4", "--benign", "0",
            "--strategies", "full", "--max-strong-calls", "1"]  # fmt: skip
    assert main(argv) == 3
    assert "stopped:" in capsys.readouterr().err


def test_cli_cascade_requires_a_strong_tier():
    with pytest.raises(SystemExit):
        main(["eval", "--judge", "cascade", "--cheap", "mock", "--families", "adjacent"])


def test_cache_cap_stops_a_single_judge_before_the_call_over_the_limit(tmp_path):
    inner = Scripted("solo", False)
    cj = CachingJudge(inner, tmp_path / "c.jsonl", max_real_calls=2)
    cj.judge([ToolOutput(0, "t", "a")])
    cj.judge([ToolOutput(1, "t", "b")])
    with pytest.raises(BudgetExceeded):
        cj.judge([ToolOutput(2, "t", "c")])
    assert inner.calls == 2
    cj.judge([ToolOutput(0, "t", "a")])  # a cache hit is still free after the cap
    assert inner.calls == 2


def test_cli_max_real_calls_stops_cleanly_and_requires_a_cache(tmp_path, capsys):
    base = ["eval", "--families", "adjacent", "--per-family", "4", "--benign", "0",
            "--strategies", "full", "--max-real-calls", "3"]  # fmt: skip
    with pytest.raises(SystemExit):
        main(base)
    assert main([*base, "--cache", str(tmp_path / "c.jsonl")]) == 3
    assert "stopped:" in capsys.readouterr().err


def test_budget_exceeded_is_not_swallowed_as_a_judge_error():
    from temporalguard.judge.base import JudgeError

    assert not issubclass(BudgetExceeded, JudgeError)
