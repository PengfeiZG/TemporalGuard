"""Render comparison rows as Markdown, CSV or JSON."""

from __future__ import annotations

import csv
import io
import json
import math
from pathlib import Path

from .metrics import EpisodeResult

COLUMNS = [
    ("strategy", "strategy"),
    ("recall", "recall"),
    ("recall_ci", "recall 95% CI"),
    ("fragment_recall", "frag_rec"),
    ("root_recall", "root_rec"),
    ("root_ci", "root 95% CI"),
    ("contained_early", "early"),
    ("precision", "prec"),
    ("fpr_output", "fpr"),
    ("fpr_ci", "fpr 95% CI"),
    ("localization", "loc"),
    ("judge_error_rate", "err"),
    ("gate_miss_rate", "gate_miss"),
    ("judge_calls_per_output", "calls/out"),
    ("tokens_per_output", "tok/out"),
    ("tokens_ci", "tok/out 95% CI"),
    ("context_per_output", "ctx/out"),
]


def _fmt(value: object) -> str:
    if isinstance(value, tuple):
        return "[" + ", ".join(_fmt(v) for v in value) + "]"
    if isinstance(value, float):
        return (
            "n/a" if math.isnan(value) else f"{value:.2f}" if abs(value) < 100 else f"{value:.0f}"
        )
    return str(value)


def _table(rows: list[dict], columns: list[tuple[str, str]]) -> str:
    header = "| " + " | ".join(label for _, label in columns) + " |"
    rule = "|" + "|".join("---" for _ in columns) + "|"
    body = ["| " + " | ".join(_fmt(r.get(key, "")) for key, _ in columns) + " |" for r in rows]
    return "\n".join([header, rule, *body])


def to_markdown(rows: list[dict]) -> str:
    present = set().union(*(r.keys() for r in rows)) if rows else set()
    return _table(rows, [(k, label) for k, label in COLUMNS if k in present or k == "strategy"])


def family_markdown(rows: list[dict]) -> str:
    """Table from `runner.family_rows`: strategies down, attack families across."""
    keys: list[str] = []
    for r in rows:
        keys += [k for k in r if k != "strategy" and k not in keys]
    return _table(rows, [("strategy", "strategy"), *[(k, k) for k in keys]])


def paired_markdown(rows: list[dict]) -> str:
    """Table of paired differences: dicts with a, b, metric, diff, lo, hi."""
    cols = [
        ("pair", "A vs B"),
        ("metric", "metric"),
        ("diff", "A - B"),
        ("ci", "95% CI"),
        ("verdict", "separable?"),
    ]
    out = []
    for r in rows:
        out.append(
            {
                "pair": f"{r['a']} vs {r['b']}",
                "metric": r["metric"],
                "diff": r["diff"],
                "ci": (r["lo"], r["hi"]),
                "verdict": "no (CI contains 0)" if r["lo"] <= 0 <= r["hi"] else "yes",
            }
        )
    return _table(out, cols)


def to_csv(rows: list[dict]) -> str:
    buf = io.StringIO()
    if rows:
        fields: list[str] = []
        for r in rows:
            fields += [k for k in r if k not in fields]
        writer = csv.DictWriter(buf, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    return buf.getvalue()


def to_json(rows: list[dict]) -> str:
    return json.dumps(rows, indent=2, default=str)


def dump_decisions(all_results: dict[str, list[EpisodeResult]], path: str | Path) -> int:
    """Write one JSON line per (strategy, episode) with the judge's reasoning, for diagnosis.

    Output text is included only for flagged outputs and true fragments, to keep files small.
    Use it to see WHY a twin was flagged or an attack missed. Returns the number of lines written.
    """
    n = 0
    with Path(path).open("w", encoding="utf-8") as fh:
        for strategy, results in all_results.items():
            for r in results:
                ep = r.episode
                truth = set(ep.attack_indices)
                decisions = []
                for d in r.decisions:
                    keep_text = d.verdict.flagged or d.output_index in truth
                    decisions.append(
                        {
                            "output_index": d.output_index,
                            "is_fragment": d.output_index in truth,
                            "verdict": d.verdict.value,
                            "stage": d.stage,
                            "risk_score": round(d.risk_score, 3),
                            "windows_examined": d.windows_examined,
                            "fragment_indices": d.fragment_indices,
                            "explanation": d.explanation,
                            "text": ep.outputs[d.output_index][1] if keep_text else None,
                        }
                    )
                fh.write(
                    json.dumps(
                        {
                            "strategy": strategy,
                            "episode_id": ep.id,
                            "family": ep.family,
                            "is_attack": ep.is_attack,
                            "task": ep.task,
                            "attack_indices": ep.attack_indices,
                            "decisions": decisions,
                        }
                    )
                    + "\n"
                )
                n += 1
    return n
