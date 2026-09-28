"""Render comparison rows as Markdown, CSV or JSON."""

from __future__ import annotations

import csv
import io
import json
import math

COLUMNS = [
    ("strategy", "strategy"),
    ("recall", "recall"),
    ("contained_early", "early"),
    ("precision", "prec"),
    ("fpr_output", "fpr"),
    ("localization", "loc"),
    ("gate_miss_rate", "gate_miss"),
    ("judge_calls_per_output", "calls/out"),
    ("tokens_per_output", "tok/out"),
    ("context_per_output", "ctx/out"),
]


def _fmt(value: object) -> str:
    if isinstance(value, float):
        return (
            "n/a" if math.isnan(value) else f"{value:.2f}" if abs(value) < 100 else f"{value:.0f}"
        )
    return str(value)


def to_markdown(rows: list[dict]) -> str:
    header = "| " + " | ".join(label for _, label in COLUMNS) + " |"
    rule = "|" + "|".join("---" for _ in COLUMNS) + "|"
    body = ["| " + " | ".join(_fmt(r.get(key, "")) for key, _ in COLUMNS) + " |" for r in rows]
    return "\n".join([header, rule, *body])


def to_csv(rows: list[dict]) -> str:
    buf = io.StringIO()
    if rows:
        writer = csv.DictWriter(buf, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return buf.getvalue()


def to_json(rows: list[dict]) -> str:
    return json.dumps(rows, indent=2, default=str)
