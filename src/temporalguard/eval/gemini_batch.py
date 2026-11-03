"""Gemini Batch API cache warmer for deterministic TemporalGuard judge windows.

Fixed strategies can be prepared in one round. Adaptive strategies use iterative
rounds: replay cached verdicts until the first missing call in each episode,
then batch those missing calls. Repeat after collecting until complete.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict
from pathlib import Path
from typing import Any, cast

from ..judge.base import BudgetExceeded, Judge, JudgeError, parse_verdict
from ..judge.cache import CachingJudge
from ..judge.prompts import SYSTEM_PROMPT, build_user_message
from ..models import ToolOutput, Usage
from ..strategies import build_guard
from .runner import _run_episode

JSON_INSTRUCTION = (
    SYSTEM_PROMPT + "\nReturn ONLY a JSON object with fields: malicious (boolean), "
    "confidence (number), needs_more_context (boolean), "
    "fragment_indices (integer array), reconstructed_instruction (string), "
    "attack_type (string), rationale (string)."
)


def request_for(window, task):
    return {
        "contents": [{"role": "user", "parts": [{"text": build_user_message(window, task)}]}],
        "systemInstruction": {"parts": [{"text": JSON_INSTRUCTION}]},
        "generationConfig": {"temperature": 0, "responseMimeType": "application/json"},
    }


class _CacheReplay(Judge):
    """Stop each episode at its first uncached judgment; never fabricate verdicts."""

    name = "gemini-batch-replay"

    def __init__(self, cache):
        self.cache = cache
        self.missing = {}

    def judge(self, window, task=None):
        if self.cache.is_cached(window, task):
            return self.cache.judge(window, task)
        key = self.cache.key_for(window, task)
        self.missing.setdefault(key, (tuple(window), task))
        raise BudgetExceeded("Uncached judgment; queue for Gemini Batch API")


def discover_windows(cache, episodes, strategies, config):
    """Replay the actual strategy with cached results and discover the next batch round.

    Every episode is restarted from the beginning on each round. Cached answers
    determine the genuine adaptive branch, so no speculative windows are billed.
    """
    replay = _CacheReplay(cache)
    incomplete = 0
    for strategy in strategies:
        for episode in episodes:
            try:
                _run_episode(strategy, replay, episode, config)
            except BudgetExceeded:
                incomplete += 1
    return replay.missing, incomplete


def prefetch_all_windows(cache, episodes, strategies, config):
    """Deterministic superset of every judge window any branch can request.

    Includes escalation and full-history confirmation windows. This can cost
    more than iterative replay, but requires only one batch submission round.
    """
    windows = {}
    for strategy in strategies:
        for episode in episodes:
            guard = build_guard(strategy, cache.inner, config=config, task=episode.task)
            limit = guard.config.max_chars_per_output
            history = []
            for index, (tool, content) in enumerate(episode.outputs):
                history.append(ToolOutput(index=index, tool=tool, content=content))
                # Gated strategies may skip calls; the superset intentionally
                # includes them rather than relying on scanner verdicts.
                sizes = guard.schedule.windows(len(history)) or [len(history)]
                if guard.config.min_window > 1:
                    sizes = [w for w in sizes if w >= guard.config.min_window] or [sizes[-1]]
                if guard.config.confirm_flags and len(history) not in sizes:
                    sizes.append(len(history))
                for size in sizes:
                    window = tuple(
                        ToolOutput(o.index, o.tool, o.content[:limit]) for o in history[-size:]
                    )
                    key = cache.key_for(window, episode.task)
                    windows.setdefault(key, (window, episode.task))
    return windows


def prefetch_shallow_windows(cache, episodes, strategies, config, depth):
    """Prefetch deterministic early windows; leave deep adaptive branches to replay.

    Per-message and full strategies are deterministic and can be completely
    prefetched. For adaptive strategies, include all scheduled windows up to
    `depth`, including confirmation windows no longer than `depth`.
    """
    if depth < 1:
        raise ValueError("prefetch depth must be >= 1")
    windows = {}
    for strategy in strategies:
        for episode in episodes:
            guard = build_guard(strategy, cache.inner, config=config, task=episode.task)
            limit = guard.config.max_chars_per_output
            history = []
            for index, (tool, content) in enumerate(episode.outputs):
                history.append(ToolOutput(index=index, tool=tool, content=content))
                sizes = guard.schedule.windows(len(history)) or [len(history)]
                if guard.config.min_window > 1:
                    sizes = [w for w in sizes if w >= guard.config.min_window] or [sizes[-1]]
                if guard.config.confirm_flags and len(history) not in sizes:
                    sizes.append(len(history))
                for size in sizes:
                    if strategy not in ("per_message", "full") and size > depth:
                        continue
                    window = tuple(
                        ToolOutput(o.index, o.tool, o.content[:limit]) for o in history[-size:]
                    )
                    key = cache.key_for(window, episode.task)
                    windows.setdefault(key, (window, episode.task))
    return windows


def _write_windows(path, windows):
    with path.open("w", encoding="utf-8") as out:
        for key, (window, task) in windows.items():
            out.write(
                json.dumps(
                    {"key": key, "task": task, "window": [asdict(item) for item in window]},
                    ensure_ascii=False,
                )
                + "\n"
            )


def _read_windows(path):
    windows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            item = json.loads(line)
            windows[item["key"]] = (tuple(ToolOutput(**x) for x in item["window"]), item["task"])
    return windows


def prepare(
    cache: CachingJudge,
    episodes,
    strategies,
    config,
    workdir,
    full_prefetch=False,
    prefetch_depth=None,
):
    workdir = Path(workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    if full_prefetch and prefetch_depth is not None:
        raise ValueError("--full-prefetch and --prefetch-depth are mutually exclusive")
    if full_prefetch:
        windows = prefetch_all_windows(cache, episodes, strategies, config)
        _, incomplete = discover_windows(cache, episodes, strategies, config)
    elif prefetch_depth is not None:
        windows = prefetch_shallow_windows(cache, episodes, strategies, config, prefetch_depth)
        needed, incomplete = discover_windows(cache, episodes, strategies, config)
        # Always include the first real missing call, even when it is deeper
        # than the selected speculative prefetch depth.
        windows.update(needed)
    else:
        windows, incomplete = discover_windows(cache, episodes, strategies, config)
    records = [
        {"key": k, "request": request_for(w, task)}
        for k, (w, task) in windows.items()
        if not cache.is_cached(w, task)
    ]
    manifest = workdir / "manifest.json"
    if manifest.exists():
        old = json.loads(manifest.read_text(encoding="utf-8"))
        if old.get("job") and not old.get("collected"):
            raise ValueError("A batch is still uncollected in this workdir; collect it first")
    with (workdir / "requests.jsonl").open("w", encoding="utf-8") as out:
        for record in records:
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
    _write_windows(workdir / "windows.jsonl", windows)
    state = {
        "model": cast(Any, cache.inner).model,
        "keys": [r["key"] for r in records],
        "distinct": len(windows),
        "already_cached": len(windows) - len(records),
        "incomplete_episodes": incomplete,
        "done": incomplete == 0,
        "full_prefetch": full_prefetch,
        "prefetch_depth": prefetch_depth,
        "job": None,
    }
    manifest.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state


def _state(workdir):
    path = Path(workdir) / "manifest.json"
    if not path.exists():
        raise ValueError("No manifest; run prepare first")
    return path, json.loads(path.read_text(encoding="utf-8"))


def submit(cache: CachingJudge, workdir):
    path, state = _state(workdir)
    if state["model"] != cast(Any, cache.inner).model:
        raise ValueError("Model does not match prepared batch")
    if state["job"]:
        raise ValueError("Already submitted; use status or collect")
    if not state["keys"]:
        return state
    client = cast(Any, cache.inner).client
    uploaded = client.files.upload(
        file=str(Path(workdir) / "requests.jsonl"), config={"mime_type": "application/jsonl"}
    )
    job = client.batches.create(
        model=state["model"],
        src=uploaded.name,
        config={"display_name": "TemporalGuard benign-twin cache warm"},
    )
    state["input_file"] = uploaded.name
    state["job"] = job.name
    path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return state


def status(cache: CachingJudge, workdir):
    _, state = _state(workdir)
    if not state["job"]:
        return "NOT_SUBMITTED", None
    job = cast(Any, cache.inner).client.batches.get(name=state["job"])
    value = getattr(getattr(job, "state", None), "name", str(getattr(job, "state", "UNKNOWN")))
    return value, job


def _download_bytes(client, filename):
    data = client.files.download(file=filename)
    if isinstance(data, bytes):
        return data
    if isinstance(data, str):
        return data.encode("utf-8")
    if hasattr(data, "read"):
        return data.read()
    raise ValueError("Unrecognized Gemini file download response")


def collect(cache: CachingJudge, episodes, strategies, config, workdir, wait=False, poll_s=30):
    path, state = _state(workdir)
    if not state["job"]:
        raise ValueError("No submitted batch")
    if state.get("collected"):
        return {"status": "ALREADY_COLLECTED", "cached": 0, "pending": False}
    windows = _read_windows(Path(workdir) / "windows.jsonl")
    expected = set(state["keys"])
    if not expected.issubset(windows):
        raise ValueError("Prepared window manifest is incomplete")
    if any(cache.key_for(w, t) != k for k, (w, t) in windows.items()):
        raise ValueError("Cache key mismatch: model, prompt, or prepared windows changed")
    if cast(Any, cache.inner).model != state["model"]:
        raise ValueError("Model does not match submitted batch")
    while True:
        label, job = status(cache, workdir)
        if "SUCCEEDED" in label or "FAILED" in label or "CANCELLED" in label or "EXPIRED" in label:
            break
        if not wait:
            return {"status": label, "cached": 0, "pending": True}
        time.sleep(poll_s)
    if "SUCCEEDED" not in label:
        return {"status": label, "cached": 0, "pending": False}
    dest = getattr(job, "dest", None)
    output = getattr(dest, "file_name", None)
    if not output:
        raise ValueError("Completed job has no output file; inspect the job in Gemini console")
    content = _download_bytes(cast(Any, cache.inner).client, output)
    (Path(workdir) / "results.jsonl").write_bytes(content)
    cached = failed = unknown = 0
    for line in content.decode("utf-8-sig").splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
            key = item.get("key")
            if key not in expected:
                unknown += 1
                continue
            response = item.get("response") or {}
            candidates = response.get("candidates") or []
            parts = (candidates[0].get("content") or {}).get("parts") or []
            raw = next(p["text"] for p in parts if "text" in p)
            window, task = windows[key]
            verdict = parse_verdict(json.loads(raw), window)
            usage = response.get("usageMetadata") or response.get("usage_metadata") or {}
            verdict.usage = Usage(
                input_tokens=int(usage.get("promptTokenCount", 0) or 0),
                output_tokens=int(usage.get("candidatesTokenCount", 0) or 0)
                + int(usage.get("thoughtsTokenCount", 0) or 0),
                calls=1,
            )
            if cache.put(window, task, verdict):
                cached += 1
        except (ValueError, KeyError, StopIteration, TypeError, IndexError, JudgeError):
            failed += 1
    state["collected"] = True
    state["cached_count"] = cached
    path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return {
        "status": label,
        "cached": cached,
        "failed": failed,
        "unknown": unknown,
        "pending": False,
    }
