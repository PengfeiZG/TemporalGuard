"""Offline tests for Gemini batch preparation and collection."""
import json
from types import SimpleNamespace

from temporalguard.eval import gemini_batch
from temporalguard.judge.cache import CachingJudge
from temporalguard.judge.gemini_judge import GeminiJudge
from temporalguard.models import ToolOutput


def test_request_uses_matching_prompt():
    from temporalguard.judge.prompts import build_user_message
    window = [ToolOutput(0, "web", "a benign message")]
    req = gemini_batch.request_for(window, "Summarize")
    assert req["contents"][0]["parts"][0]["text"] == build_user_message(window, "Summarize")
    assert req["generationConfig"]["responseMimeType"] == "application/json"


def test_prepare_submit_collect_mocked(tmp_path, monkeypatch):
    window = (ToolOutput(0, "web", "a benign message"),)
    client = SimpleNamespace()
    client.files = SimpleNamespace(
        upload=lambda **kw: SimpleNamespace(name="files/input"),
        download=lambda **kw: b"",
    )
    client.batches = SimpleNamespace(
        create=lambda **kw: SimpleNamespace(name="batches/123"),
        get=lambda **kw: SimpleNamespace(state=SimpleNamespace(name="JOB_STATE_SUCCEEDED"),
                                         dest=SimpleNamespace(file_name="files/output")),
    )
    cache = CachingJudge(GeminiJudge(model="gemini-test", client=client), tmp_path / "cache.jsonl")
    monkeypatch.setattr(gemini_batch, "discover_windows", lambda *args: ({
        cache.key_for(window, "Summarize"): (window, "Summarize")}, 1))
    result = gemini_batch.prepare(cache, [], ["full"], None, tmp_path / "job")
    assert len(result["keys"]) == 1
    assert json.loads((tmp_path / "job" / "requests.jsonl").read_text())["key"] == result["keys"][0]
    assert gemini_batch.submit(cache, tmp_path / "job")["job"] == "batches/123"
    payload = {"key": result["keys"][0], "response": {
        "candidates": [{"content": {"parts": [{"text": json.dumps({
            "malicious": False, "confidence": 0.99, "needs_more_context": False,
            "fragment_indices": [], "reconstructed_instruction": "",
            "attack_type": "none", "rationale": "ordinary content"})}]}}],
        "usageMetadata": {"promptTokenCount": 21, "candidatesTokenCount": 10}}}
    client.files.download = lambda **kw: (json.dumps(payload) + "\n").encode()
    report = gemini_batch.collect(cache, [], ["full"], None, tmp_path / "job")
    assert report["cached"] == 1
    assert cache.is_cached(window, "Summarize")
    assert cache.judge(window, "Summarize").malicious is False


def test_adaptive_replay_discovers_real_cached_branch(tmp_path):
    from temporalguard.config import EngineConfig
    from temporalguard.eval.episodes import Episode
    from temporalguard.models import JudgeResult
    cache = CachingJudge(GeminiJudge(model="gemini-test", client=SimpleNamespace()),
                         tmp_path / "cache.jsonl")
    outputs = [ToolOutput(i, "web", "suspicious instruction " + str(i)) for i in range(4)]
    ep = Episode("example", "li", "Summarize", [(x.tool, x.content) for x in outputs], [3])
    strategies = ["fib_min3_fallback_confirm"]
    missing, incomplete = gemini_batch.discover_windows(cache, [ep], strategies, EngineConfig())
    assert incomplete > 0 and missing
    for _ in range(20):
        for window, task in missing.values():
            cache.put(window, task, JudgeResult(malicious=False, confidence=0.2,
                                               needs_more_context=True))
        missing, incomplete = gemini_batch.discover_windows(cache, [ep], strategies, EngineConfig())
        if not missing:
            break
    assert incomplete == 0 and not missing
