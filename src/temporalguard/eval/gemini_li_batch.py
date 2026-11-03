"""Unified Gemini Batch API cache warmer for Pro baseline and LogicInception A/B.

Commands: prepare, submit, status, collect. Never makes synchronous model calls.
Run `temporalguard eval` normally after prepare reports zero missing requests.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import asdict
from pathlib import Path

from temporalguard.config import EngineConfig
from temporalguard.eval.episodes import build_suite
from temporalguard.eval.runner import _run_episode
from temporalguard.judge.base import parse_verdict
from temporalguard.judge.cache import CachingJudge
from temporalguard.judge.gemini_judge import GeminiJudge
from temporalguard.judge.prompts import SYSTEM_PROMPT, build_user_message
from temporalguard.models import Usage

DEFAULT_MODEL = "gemini-3.1-flash-lite"
SYSTEM = (
    SYSTEM_PROMPT + "\nReturn ONLY a JSON object with fields: malicious (boolean), "
    "confidence (number), needs_more_context (boolean), "
    "fragment_indices (integer array), reconstructed_instruction (string), "
    "attack_type (string), rationale (string)."
)


class NeedsBatch(Exception):
    pass


class DiscoveryJudge(CachingJudge):
    """Replay strategy using cached answers; stop an episode at its first missing verdict."""

    def __init__(self, inner, path):
        super().__init__(inner, path)
        self.missing = {}

    def judge(self, window, task=None):
        key = self._key(window, task)
        if key in self._store:
            return super().judge(window, task)
        self.missing[key] = {
            "key": key,
            "indices": [o.index for o in window],
            "request": {
                "contents": [
                    {"role": "user", "parts": [{"text": build_user_message(window, task)}]}
                ],
                "config": {
                    "system_instruction": SYSTEM,
                    "response_mime_type": "application/json",
                    "temperature": 0.0,
                },
            },
        }
        raise NeedsBatch()


def paths(args):
    directory = Path(args.workdir)
    directory.mkdir(parents=True, exist_ok=True)
    return directory, directory / "pending.json", directory / "job.json"


def prefetch_per_message(judge, episodes, config):
    """Prefetch all Fixed(1), ungated, no-confirm windows without fake verdicts.

    The per_message strategy evaluates precisely one current-output window for
    every output. It does not depend on earlier judge results, so this list is
    complete and exact for the currently configured strategy.
    """
    from temporalguard.models import ToolOutput
    from temporalguard.schedules import Fixed
    from temporalguard.strategies import STRATEGIES

    strategy = STRATEGIES["per_message"]
    if (
        not isinstance(strategy.schedule, Fixed)
        or strategy.schedule.windows(2) != [1]
        or strategy.gate
        or strategy.confirm
        or strategy.min_window != 1
        or config.confirm_flags
        or config.min_window != 1
    ):
        raise SystemExit("per_message configuration changed; refusing unsafe prefetch.")
    for ep in episodes:
        for index, (tool, content) in enumerate(ep.outputs):
            window = [
                ToolOutput(index=index, tool=tool, content=content[: config.max_chars_per_output])
            ]
            try:
                judge.judge(window, ep.task)
            except NeedsBatch:
                pass


def prefetch_full(judge, episodes, config):
    """Prefetch every full-history window for the ungated `full` strategy.

    These windows are deterministic and do not depend on previous verdicts.
    """
    from temporalguard.models import ToolOutput
    from temporalguard.schedules import Full
    from temporalguard.strategies import STRATEGIES

    strategy = STRATEGIES["full"]
    if (
        not isinstance(strategy.schedule, Full)
        or strategy.gate
        or strategy.confirm
        or strategy.min_window != 1
        or config.confirm_flags
        or config.min_window != 1
    ):
        raise SystemExit("full configuration changed; refusing unsafe prefetch.")
    for ep in episodes:
        history = []
        for index, (tool, content) in enumerate(ep.outputs):
            history.append(
                ToolOutput(index=index, tool=tool, content=content[: config.max_chars_per_output])
            )
            try:
                judge.judge(list(history), ep.task)
            except NeedsBatch:
                pass


def prefetch_fib_first(judge, episodes, config):
    """Prefetch only unconditional first judge windows for the ungated Fibonacci strategy.

    No simulated verdicts. Escalation and confirmation windows remain exact-only.
    """
    from temporalguard.models import ToolOutput
    from temporalguard.schedules import Fibonacci, WithFullFallback
    from temporalguard.strategies import STRATEGIES

    strategy = STRATEGIES["fib_min3_fallback_confirm"]
    if (
        strategy.gate
        or not strategy.confirm
        or strategy.min_window != 3
        or not isinstance(strategy.schedule, WithFullFallback)
        or not isinstance(strategy.schedule.inner, Fibonacci)
        or config.min_window != 1
    ):
        raise SystemExit("Fibonacci strategy configuration changed; refusing unsafe prefetch.")

    for ep in episodes:
        history = []
        for index, (tool, content) in enumerate(ep.outputs):
            history.append(ToolOutput(index=index, tool=tool, content=content))
            n = len(history)
            sizes = strategy.schedule.windows(n) or [n]
            effective_min = max(config.min_window, strategy.min_window)
            if effective_min > 1:
                sizes = [w for w in sizes if w >= effective_min] or [sizes[-1]]
            window = [
                ToolOutput(o.index, o.tool, o.content[: config.max_chars_per_output])
                for o in history[-sizes[0] :]
            ]
            try:
                judge.judge(window, ep.task)
            except NeedsBatch:
                pass


def prepare(args):
    directory, pending, job = paths(args)
    if job.exists():
        raise SystemExit("A job.json exists. Collect that batch before preparing another round.")
    if args.profile != "pro-baseline":
        os.environ["TEMPORALGUARD_LI_FILE"] = str(Path("data") / f"li_attacks_{args.dataset}.csv")
    judge = DiscoveryJudge(GeminiJudge(model=args.model, client=object()), args.cache)
    families = (
        ["agentdojo_span"] if args.profile == "pro-baseline" else ["li", "li_span", "li_concat"]
    )
    episodes = build_suite(args.seed, args.per_family, 0, families, twins=False)
    finished = 0
    blocked = 0
    for strategy in args.strategies:
        for ep in episodes:
            try:
                _run_episode(strategy, judge, ep, EngineConfig())
                finished += 1
            except NeedsBatch:
                blocked += 1
    exact_count = len(judge.missing)
    config = EngineConfig()
    before = len(judge.missing)
    if "per_message" in args.strategies:
        prefetch_per_message(judge, episodes, config)
    if "full" in args.strategies:
        prefetch_full(judge, episodes, config)
    if "fib_min3_fallback_confirm" in args.strategies:
        prefetch_fib_first(judge, episodes, config)
    print(
        f"Deterministic prefetch: {len(judge.missing) - before} additional windows; "
        f"exact frontier: {exact_count}."
    )
    requests = list(judge.missing.values())
    if requests:
        pending.write_text(json.dumps(requests, indent=2), encoding="utf-8")
    elif pending.exists():
        pending.unlink()
    print(
        f"Cached complete strategy/episode pairs: "
        f"{finished}/{len(episodes) * len(args.strategies)}; blocked: {blocked}"
    )
    print(f"New distinct windows ready for batch: {len(requests)}")
    if requests:
        print(
            f"Prepared {pending}. Run: temporalguard gemini-batch submit --profile {args.profile}"
        )
    else:
        print("ALL READY. Run the normal TemporalGuard eval commands for final metrics.")


def client():
    if not os.environ.get("GEMINI_API_KEY"):
        raise SystemExit("GEMINI_API_KEY environment variable is missing")
    try:
        from google import genai
    except ImportError as exc:
        raise SystemExit('Install SDK: pip install -e ".[gemini]"') from exc
    return genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def submit(args):
    directory, pending, jobfile = paths(args)
    if jobfile.exists():
        raise SystemExit("Existing job.json: collect it first to avoid duplicate charges.")
    if not pending.exists():
        raise SystemExit("No pending.json; run prepare first.")
    rows = json.loads(pending.read_text(encoding="utf-8"))
    if not rows:
        raise SystemExit("No pending requests.")
    # Keep the SDK client alive for the entire request.
    with client() as c:
        batch = c.batches.create(
            model=args.model,
            src=[r["request"] for r in rows],
            config={"display_name": f"temporalguard-{args.profile}-batch"},
        )
    # Save keys and windows in exact inline order, required for parsing and cache compatibility.
    jobfile.write_text(
        json.dumps(
            {"name": batch.name, "rows": rows, "model": args.model, "profile": args.profile},
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"SUBMITTED: {batch.name} ({len(rows)} requests).")
    print("Run status or collect later; no synchronous generation was used.")


def status(args):
    _, _, jobfile = paths(args)
    if not jobfile.exists():
        raise SystemExit("No active job.json.")
    job = json.loads(jobfile.read_text(encoding="utf-8"))
    # Do not chain client().batches.get(...): the temporary client can be
    # garbage-collected/closed before the SDK finishes the request.
    with client() as c:
        batch = c.batches.get(name=job["name"])
        state = batch.state
    print(f"{job['name']}: {state}")


def _response_text(response):
    if response is None:
        return None
    if getattr(response, "text", None):
        return response.text
    # SDK response may expose only candidates/parts, particularly with batch jobs.
    candidates = getattr(response, "candidates", None) or []
    if candidates:
        parts = getattr(getattr(candidates[0], "content", None), "parts", None) or []
        return "".join(getattr(p, "text", "") or "" for p in parts)
    return None


def collect(args):
    directory, pending, jobfile = paths(args)
    if not jobfile.exists():
        raise SystemExit("No active job.json.")
    info = json.loads(jobfile.read_text(encoding="utf-8"))
    if info.get("profile", args.profile) != args.profile:
        raise SystemExit("Profile mismatch with submitted job.")
    # Retain the client while retrieving and parsing the entire response.
    with client() as c:
        batch = c.batches.get(name=info["name"])
        state = batch.state.name if hasattr(batch.state, "name") else str(batch.state)
        # Copy response data before closing the client.
        dest = getattr(batch, "dest", None)
        responses = getattr(dest, "inlined_responses", None)
    print(f"{info['name']}: {state}")
    if state not in (
        "JOB_STATE_SUCCEEDED",
        "JOB_STATE_FAILED",
        "JOB_STATE_CANCELLED",
        "JOB_STATE_EXPIRED",
    ):
        print("Still processing. Try collect later.")
        return
    if state != "JOB_STATE_SUCCEEDED":
        raise SystemExit("Job not successful; preserving job.json for investigation.")
    if responses is None:
        raise SystemExit("Batch returned no inline responses; preserving job.json.")
    if len(responses) != len(info["rows"]):
        raise SystemExit("Batch response count mismatch; preserving job.json.")
    cache = Path(args.cache)
    cache.parent.mkdir(parents=True, exist_ok=True)
    existing = CachingJudge(
        GeminiJudge(model=info.get("model", args.model), client=object()), cache
    )
    written = 0
    failed = 0
    with cache.open("a", encoding="utf-8") as out:
        for row, item in zip(info["rows"], responses, strict=False):
            if row["key"] in existing._store:
                continue
            response = getattr(item, "response", None)
            rawtext = _response_text(response)
            if not rawtext:
                failed += 1
                continue
            try:
                from temporalguard.models import ToolOutput

                # parse_verdict needs only absolute indices, not original content.
                window = [ToolOutput(index=i, tool="batch", content="") for i in row["indices"]]
                verdict = parse_verdict(json.loads(rawtext), window)
                usage = getattr(response, "usage_metadata", None)
                verdict.usage = Usage(
                    input_tokens=int(getattr(usage, "prompt_token_count", 0) or 0),
                    output_tokens=int(getattr(usage, "candidates_token_count", 0) or 0)
                    + int(getattr(usage, "thoughts_token_count", 0) or 0),
                    calls=1,
                    latency_s=0.0,
                )
                out.write(json.dumps({"key": row["key"], "result": asdict(verdict)}) + "\n")
                existing._store[row["key"]] = asdict(verdict)
                written += 1
            except (ValueError, TypeError, AttributeError) as exc:
                failed += 1
                print(f"Invalid response for {row['key'][:12]}: {exc}", file=sys.stderr)
    # Keep immutable audit record of submitted job before clearing active marker.
    audit = directory / f"completed_{info['name'].replace('/', '_')}.json"
    audit.write_text(
        json.dumps(
            {
                "name": info["name"],
                "imported": written,
                "failed": failed,
                "count": len(info["rows"]),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    jobfile.unlink()
    print(f"Imported {written} valid judgments; {failed} failed. Cache: {cache}")
    print("Run prepare again to discover the next required windows.")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=["prepare", "submit", "status", "collect"])
    p.add_argument("--dataset", choices=["A", "B"], required=True)
    p.add_argument("--model", default=DEFAULT_MODEL)
    p.add_argument(
        "--strategies",
        nargs="+",
        default=["per_message"],
        choices=["per_message", "full", "fib_min3_fallback_confirm"],
    )
    p.add_argument("--per-family", type=int, default=12)
    p.add_argument("--cache", default="runs/cache_gemini_flash_lite.jsonl")
    p.add_argument("--workdir", default=None)
    p.add_argument("--seed", type=int, default=0)
    args = p.parse_args()
    args.profile = f"li-{args.dataset.lower()}"
    if args.workdir is None:
        args.workdir = f"runs/gemini_li_{args.dataset.lower()}_batch"
    if args.action == "prepare":
        path = Path("data") / f"li_attacks_{args.dataset}.csv"
        if not path.exists():
            p.error(f"Missing dataset: {path}")
    {"prepare": prepare, "submit": submit, "status": status, "collect": collect}[args.action](args)


if __name__ == "__main__":
    main()
