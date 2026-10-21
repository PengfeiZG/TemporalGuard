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
from collections.abc import Sequence
from dataclasses import asdict
from pathlib import Path

from ..models import JudgeResult, ToolOutput, Usage
from .base import Judge
from .prompts import SYSTEM_PROMPT, build_user_message


def _to_result(raw: dict) -> JudgeResult:
    usage = Usage(**raw.pop("usage"))
    return JudgeResult(**raw, usage=usage)


class CachingJudge(Judge):
    def __init__(self, inner: Judge, path: str | Path | None = None) -> None:
        self.inner = inner
        self.name = f"cached-{inner.name}"
        self.path = Path(path) if path else None
        self.hits = 0
        self.misses = 0
        self._store: dict[str, dict] = {}
        if self.path and self.path.exists():
            for line in self.path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    entry = json.loads(line)
                    self._store[entry["key"]] = entry["result"]

    def _key(self, window: Sequence[ToolOutput], task: str | None) -> str:
        model = getattr(self.inner, "model", self.inner.name)
        effort = getattr(self.inner, "reasoning_effort", None)
        payload = json.dumps(
            [self.inner.name, model, effort, SYSTEM_PROMPT, build_user_message(window, task)]
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()

    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        key = self._key(window, task)
        if key in self._store:
            self.hits += 1
            return _to_result(json.loads(json.dumps(self._store[key])))
        result = self.inner.judge(window, task)  # JudgeError propagates and is never cached
        self.misses += 1
        raw = asdict(result)
        self._store[key] = raw
        if self.path:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({"key": key, "result": raw}) + "\n")
        return result
