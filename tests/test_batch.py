"""Tests for the batch path: same requests as the normal judge, answers land in the same cache."""

from types import SimpleNamespace

import pytest

from temporalguard.cli import main
from temporalguard.config import EngineConfig
from temporalguard.eval import batch
from temporalguard.eval.episodes import build_suite
from temporalguard.eval.runner import run_many
from temporalguard.judge.anthropic_judge import AnthropicJudge
from temporalguard.judge.cache import CachingJudge

VERDICT = {"malicious": False, "confidence": 0.9, "needs_more_context": False}


def tool_message(payload=None):
    block = SimpleNamespace(type="tool_use", input=payload or VERDICT)
    usage = SimpleNamespace(input_tokens=120, output_tokens=15)
    return SimpleNamespace(content=[block], usage=usage, stop_reason="tool_use")


class FakeBatches:
    def __init__(self):
        self.created = []
        self.status = "ended"
        self.items = []
        self.ids = {}

    def create(self, requests):
        self.created.append(requests)
        batch_id = f"batch_{len(self.created)}"
        self.ids[batch_id] = {r["custom_id"] for r in requests}
        return SimpleNamespace(id=batch_id)

    def retrieve(self, batch_id):
        return SimpleNamespace(processing_status=self.status)

    def results(self, batch_id):  # like the real API: only the results of this batch
        return [i for i in self.items if i.custom_id in self.ids[batch_id]]


class FakeClient:
    def __init__(self):
        self.sync_requests = []
        self.messages = SimpleNamespace(create=self._create, batches=FakeBatches())

    def _create(self, **request):
        self.sync_requests.append(request)
        return tool_message()


@pytest.fixture
def setup(tmp_path):
    client = FakeClient()
    inner = AnthropicJudge(model="claude-haiku-5-5", client=client)
    cache = CachingJudge(inner, path=tmp_path / "cache.jsonl")
    episodes = build_suite(seed=0, per_family=2, benign=0, families=["adjacent"], twins=False)
    return client, cache, episodes, EngineConfig()


def succeeded(custom_id, payload=None):
    return SimpleNamespace(
        custom_id=custom_id, result=SimpleNamespace(type="succeeded", message=tool_message(payload))
    )


def test_recorded_windows_are_distinct_and_cover_the_run(setup):
    client, cache, episodes, config = setup
    windows = batch.collect_windows(cache, episodes, ["per_message"], config)
    assert 0 < len(windows) <= sum(len(e.outputs) for e in episodes)
    full = batch.collect_windows(cache, episodes, ["full"], config)
    assert len(full) >= 1 and client.sync_requests == []  # recording makes no API calls


def test_strategies_that_depend_on_earlier_answers_are_refused(setup):
    _, cache, episodes, config = setup
    with pytest.raises(ValueError, match="cannot batch"):
        batch.collect_windows(cache, episodes, ["fib_min3_fallback_confirm"], config)


@pytest.mark.parametrize("model", ["claude-haiku-5-5", "claude-sonnet-5-5"])
def test_the_batch_request_is_identical_to_the_one_the_normal_judge_sends(model):
    client = FakeClient()
    judge = AnthropicJudge(model=model, client=client)
    episodes = build_suite(seed=0, per_family=1, benign=0, families=["adjacent"], twins=False)
    cache = CachingJudge(judge)
    windows = batch.collect_windows(cache, episodes, ["full"], EngineConfig())
    (window, task) = next(iter(windows.values()))
    judge.judge(window, task)
    assert client.sync_requests[0] == judge.build_request(window, task)
    assert ("thinking" in client.sync_requests[0]) == (model == "claude-sonnet-5-5")


def test_submit_skips_cached_windows_and_uses_the_cache_key_as_id(setup):
    client, cache, episodes, config = setup
    windows = batch.collect_windows(cache, episodes, ["per_message"], config)
    first_key, (w, t) = next(iter(windows.items()))
    cache.inner.client = client
    cache.put(w, t, batch.RecordingJudge().judge(w, t))
    report = batch.submit(cache, windows)
    assert report.already_cached == 1 and report.submitted == len(windows) - 1
    ids = [r["custom_id"] for r in client.messages.batches.created[0]]
    assert first_key not in ids and len(ids) == len(set(ids))
    assert all(len(i) == 64 for i in ids)  # sha256 hex, within the 64-character limit


def test_limit_submits_only_a_small_test(setup):
    client, cache, episodes, config = setup
    windows = batch.collect_windows(cache, episodes, ["per_message"], config)
    report = batch.submit(cache, windows, limit=3)
    assert report.submitted == 3 and len(client.messages.batches.created[0]) == 3


def test_collected_answers_make_the_normal_run_free(setup):
    client, cache, episodes, config = setup
    windows = batch.collect_windows(cache, episodes, ["per_message", "full"], config)
    batch.submit(cache, windows)
    client.messages.batches.items = [
        succeeded(r["custom_id"]) for r in client.messages.batches.created[0]
    ]
    done = batch.collect(cache, windows)
    assert done.cached == len(windows) and not done.pending
    results = run_many(cache, episodes, ["per_message", "full"], config)
    assert cache.misses == 0 and client.sync_requests == []
    assert results["per_message"] and results["full"]


def test_failed_and_text_only_results_are_left_for_the_normal_run(setup):
    client, cache, episodes, config = setup
    windows = batch.collect_windows(cache, episodes, ["per_message"], config)
    batch.submit(cache, windows)
    ids = [r["custom_id"] for r in client.messages.batches.created[0]]
    text_only = SimpleNamespace(
        content=[SimpleNamespace(type="text", text="benign")],
        usage=SimpleNamespace(input_tokens=1, output_tokens=1),
    )
    client.messages.batches.items = [
        SimpleNamespace(custom_id=ids[0], result=SimpleNamespace(type="errored")),
        SimpleNamespace(
            custom_id=ids[1], result=SimpleNamespace(type="succeeded", message=text_only)
        ),
        *[succeeded(i) for i in ids[2:]],
    ]
    done = batch.collect(cache, windows)
    assert done.not_succeeded == 1 and done.no_verdict == 1 and done.cached == len(ids) - 2
    run_many(cache, episodes, ["per_message"], config)
    assert cache.misses == 2  # exactly the two that did not come back are judged normally


def test_an_unfinished_batch_is_kept_for_later(setup):
    client, cache, episodes, config = setup
    windows = batch.collect_windows(cache, episodes, ["per_message"], config)
    batch.submit(cache, windows)
    client.messages.batches.status = "in_progress"
    waiting = batch.collect(cache, windows)
    assert waiting.pending == ["batch_1"] and waiting.cached == 0
    client.messages.batches.status = "ended"
    client.messages.batches.items = [
        succeeded(r["custom_id"]) for r in client.messages.batches.created[0]
    ]
    assert batch.collect(cache, windows).cached == len(windows)
    assert batch.collect(cache, windows).cached == 0  # already collected, nothing repeated


def test_cli_refuses_strategies_that_cannot_be_batched_and_other_judges(capsys):
    assert main(["batch-warm", "--judge", "anthropic", "--cache", "x.jsonl"]) == 2
    assert main(["batch-warm", "--strategies", "fib", "--judge", "anthropic"]) == 2
    assert main(["batch-warm", "--strategies", "full", "--judge", "mock"]) == 2
    assert "batch-warm needs" in capsys.readouterr().err


def test_two_runs_can_share_the_batch_state_without_losing_either(setup, tmp_path):
    client, cache, episodes, config = setup
    other_episodes = build_suite(seed=1, per_family=2, benign=0, families=["spaced"], twins=False)
    win_a = batch.collect_windows(cache, episodes, ["per_message"], config)
    win_b = batch.collect_windows(cache, other_episodes, ["per_message"], config)
    only_b = {k: v for k, v in win_b.items() if k not in win_a}
    assert only_b  # the two runs really differ
    batch.submit(cache, win_a)
    batch.submit(cache, {k: v for k, v in win_b.items() if k not in win_a})
    created = client.messages.batches.created
    client.messages.batches.items = [succeeded(r["custom_id"]) for part in created for r in part]
    first = batch.collect(cache, win_a)  # collects run A; run B's batch must stay open
    assert first.cached == len(win_a) and first.unknown == len(only_b)
    second = batch.collect(cache, win_b)
    assert second.cached == len(only_b)
    assert batch.collect(cache, win_b).cached == 0  # everything now collected
