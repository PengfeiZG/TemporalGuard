"""Run the judge through Anthropic's Message Batches API (half price, results within 24 hours).

Only strategies whose windows do not depend on earlier answers can be batched: `per_message`,
`fixed5` and `full` ask for the same windows whatever the judge says. This module records those
windows, submits them as one batch, and, once the batch has ended, writes each verdict into the
same cache file the normal judge uses. A later `eval` run with the same arguments is then served
from the cache. Windows that failed in the batch are not cached; `eval` simply judges them one
at a time.
"""

from __future__ import annotations

import json
import threading
import time
from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path

from ..config import EngineConfig
from ..judge.base import Judge, JudgeError, parse_verdict
from ..judge.cache import CachingJudge
from ..models import JudgeResult, ToolOutput, Usage
from .episodes import Episode
from .runner import run_many

BATCHABLE = ("per_message", "fixed5", "full")


class RecordingJudge(Judge):
    """Answers 'benign, confident' and remembers every window it was asked about."""

    name = "recording"

    def __init__(self) -> None:
        self.calls: list[tuple[tuple[ToolOutput, ...], str | None]] = []
        self._lock = threading.Lock()

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        with self._lock:
            self.calls.append((tuple(window), task))
        return JudgeResult(
            malicious=False,
            confidence=0.99,
            needs_more_context=False,
            rationale="recorded",
            usage=Usage(calls=1),
        )


def collect_windows(
    cache: CachingJudge,
    episodes: Sequence[Episode],
    strategies: Sequence[str],
    config: EngineConfig,
) -> dict[str, tuple[tuple[ToolOutput, ...], str | None]]:
    """Every distinct window the strategies would send, keyed by cache key."""
    bad = [s for s in strategies if s not in BATCHABLE]
    if bad:
        raise ValueError(
            f"cannot batch {bad}: their windows depend on earlier answers; "
            f"batchable strategies are {list(BATCHABLE)}"
        )
    recorder = RecordingJudge()
    run_many(recorder, episodes, list(strategies), config, workers=1)
    windows: dict[str, tuple[tuple[ToolOutput, ...], str | None]] = {}
    for window, task in recorder.calls:
        windows.setdefault(cache.key_for(window, task), (window, task))
    return windows


@dataclass
class SubmitReport:
    distinct: int = 0
    already_cached: int = 0
    submitted: int = 0
    batch_ids: list[str] = field(default_factory=list)


def _state_path(cache: CachingJudge) -> Path:
    if cache.path is None:
        raise ValueError("batching needs --cache, which is where the answers are stored")
    return cache.path.with_name(cache.path.name + ".batches.json")


def _load_state(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"batches": []}


def submit(
    cache: CachingJudge,
    windows: dict[str, tuple[tuple[ToolOutput, ...], str | None]],
    limit: int | None = None,
    chunk: int = 2000,
) -> SubmitReport:
    """Submit every window that is not cached yet. `limit` submits only the first N (a test)."""
    inner = cache.inner
    client = getattr(inner, "client", None)
    if client is None or not hasattr(inner, "build_request"):
        raise ValueError("batching needs --judge anthropic")
    report = SubmitReport(distinct=len(windows))
    todo = []
    for key, (window, task) in windows.items():
        if cache.is_cached(window, task):
            report.already_cached += 1
        else:
            todo.append({"custom_id": key, "params": inner.build_request(window, task)})
    if limit is not None:
        todo = todo[:limit]
    state_file = _state_path(cache)
    state = _load_state(state_file)
    for start in range(0, len(todo), chunk):
        part = todo[start : start + chunk]
        batch = client.messages.batches.create(requests=part)
        report.batch_ids.append(batch.id)
        report.submitted += len(part)
        state["batches"].append({"id": batch.id, "requests": len(part), "collected": False})
        state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return report


@dataclass
class CollectReport:
    pending: list[str] = field(default_factory=list)
    cached: int = 0
    not_succeeded: int = 0
    no_verdict: int = 0
    unknown: int = 0
    counts: dict[str, int] = field(default_factory=dict)


def collect(
    cache: CachingJudge,
    windows: dict[str, tuple[tuple[ToolOutput, ...], str | None]],
    wait: bool = False,
    poll_s: float = 30.0,
    log: Callable[[str], None] | None = None,
) -> CollectReport:
    """Write the verdicts of every finished, uncollected batch into the cache."""
    client = getattr(cache.inner, "client", None)
    if client is None:
        raise ValueError("batching needs --judge anthropic")
    state_file = _state_path(cache)
    state = _load_state(state_file)
    report = CollectReport()
    for entry in state["batches"]:
        if entry["collected"]:
            continue
        while True:
            batch = client.messages.batches.retrieve(entry["id"])
            status = getattr(batch, "processing_status", "")
            if status == "ended" or not wait:
                break
            if log:
                log(f"batch {entry['id']}: {status}, waiting {poll_s:.0f}s ...")
            time.sleep(poll_s)
        if status != "ended":
            report.pending.append(entry["id"])
            continue
        foreign = 0  # answers for windows of a different run (another variant or family)
        for item in client.messages.batches.results(entry["id"]):
            result = item.result
            found = windows.get(item.custom_id)
            if found is None:
                foreign += 1
                continue
            report.counts[result.type] = report.counts.get(result.type, 0) + 1
            if result.type != "succeeded":
                report.not_succeeded += 1
                continue
            window, task = found
            message = result.message
            block = next((b for b in message.content if getattr(b, "type", "") == "tool_use"), None)
            if block is None:
                report.no_verdict += 1  # the model answered in text; eval will retry it
                continue
            try:
                verdict = parse_verdict(block.input, window)
            except JudgeError:
                report.no_verdict += 1
                continue
            usage = getattr(message, "usage", None)
            verdict.usage = Usage(
                input_tokens=int(getattr(usage, "input_tokens", 0) or 0),
                output_tokens=int(getattr(usage, "output_tokens", 0) or 0),
                calls=1,
            )
            if cache.put(window, task, verdict):
                report.cached += 1
        report.unknown += foreign
        if foreign == 0:  # a batch holding other runs' windows stays open for their collect
            entry["collected"] = True
            state_file.write_text(json.dumps(state, indent=2), encoding="utf-8")
    return report
