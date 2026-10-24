"""Disk-backed cache for judge verdicts.

Strategies in a comparison repeatedly ask the judge about identical windows (every strategy that
starts at window size 1 sends the same first call). The cache stores each verdict keyed by the
exact prompt, so real API spend is paid once per distinct window, and runs are reproducible
because a window always gets the same verdict.

A cache hit returns the ORIGINAL usage (tokens, latency) of the call that produced it. That keeps
the cost metrics describing what each strategy would cost uncached, so strategies stay
comparable. Real spend is `misses`, not the reported token totals.
"""

from __future__ import annotations

import hashlib
import json
import threading
from collections.abc import Sequence
from dataclasses import asdict
from pathlib import Path

from ..models import JudgeResult, ToolOutput, Usage
from .base import BudgetExceeded, Judge
from .prompts import SYSTEM_PROMPT, build_user_message


def _to_result(raw: dict) -> JudgeResult:
    usage = Usage(**raw.pop("usage"))
    return JudgeResult(**raw, usage=usage)


class CachingJudge(Judge):
    def __init__(
        self, inner: Judge, path: str | Path | None = None, max_real_calls: int | None = None
    ) -> None:
        self.inner = inner
        self.max_real_calls = max_real_calls  # hard cap on REAL calls; cache hits are free
        self.name = f"cached-{inner.name}"
        self.path = Path(path) if path else None
        self.hits = 0
        self.misses = 0
        self._lock = threading.Lock()  # episodes may be judged by several worker threads
        self._store: dict[str, dict] = {}
        self.skipped_lines = 0
        if self.path and self.path.exists():
            text = self.path.read_text(encoding="utf-8")
            for line in text.splitlines():
                if not line.strip():
                    continue
                try:
                    entry = json.loads(line)
                    self._store[entry["key"]] = entry["result"]
                except (ValueError, KeyError, TypeError):
                    # e.g. a line cut short by Ctrl+C: skip it, the call will simply be repeated
                    self.skipped_lines += 1
            if text and not text.endswith("\n"):
                # the next append must start on a fresh line, or it would join the cut-short one
                with self.path.open("a", encoding="utf-8") as fh:
                    fh.write("\n")

    def _key(self, window: Sequence[ToolOutput], task: str | None) -> str:
        model = getattr(self.inner, "model", self.inner.name)
        effort = getattr(self.inner, "reasoning_effort", None)
        parts = [self.inner.name, model, effort, SYSTEM_PROMPT, build_user_message(window, task)]
        if getattr(self.inner, "tool_choice_mode", "forced") == "auto":
            parts.append("tool_choice=auto")  # only added when set, so older cache keys stay valid
        payload = json.dumps(parts)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def is_cached(self, window: Sequence[ToolOutput], task: str | None = None) -> bool:
        """True if judging this window would be served from the cache (free)."""
        with self._lock:
            return self._key(window, task) in self._store

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        key = self._key(window, task)
        with self._lock:
            cached = self._store.get(key)
            if cached is not None:
                self.hits += 1
        if cached is not None:
            return _to_result(json.loads(json.dumps(cached)))
        if self.max_real_calls is not None and self.misses >= self.max_real_calls:
            raise BudgetExceeded(
                f"reached the cap of {self.max_real_calls} real calls; raise --max-real-calls and "
                "rerun the same command to continue from the cache"
            )
        result = self.inner.judge(window, task)  # JudgeError propagates and is never cached
        raw = asdict(result)
        with self._lock:
            self.misses += 1
            self._store[key] = raw
            if self.path:
                self.path.parent.mkdir(parents=True, exist_ok=True)
                with self.path.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"key": key, "result": raw}) + "\n")
        return result
