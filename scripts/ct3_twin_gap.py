"""Attack-versus-twin gap tables for cross-tool v3 (and, with --version ct4, v4), from the dumps of `temporalguard eval ... --dump`.

Expects `runs/ct3_<judge>_dump.jsonl` for judge stems claude (Haiku), openai (Luna), sonnet, sol, gemini_pro and gemini_flash
(Flash-Lite), from runs over the families ct3, ct3_span and ct3_concat, 12 sessions each, with all three strategies.

Tables: the gap (attack flagged minus twin flagged, counting only flags on the chain's own text) over all twelve scenarios, over the
eight the probe models acted on (ct3_data.FOLLOWED) and over the other four; and, for single reads, how often each part (F1, F2, F3)
is flagged ALONE in the attack and in the twin. The last table answers whether F1 is flagged simply because its target differs from
the task's, which would make any gain from context unrelated to cross-tool reasoning.

Usage (from the repository root):  python scripts/ct3_twin_gap.py [--version ct4] [--out runs/ct3_twin_gap_summary.md]
With --version ct4 it reads runs/ct4_<judge>_dump.jsonl and runs/ct4_probe_<model>.md; v4's changed record is F2, so the part table
should show F2 alone flagged in the attack no more often than in the twin (+AI: --version added 2 Nov 2026).
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from li_twin_gap import JUDGES, SHORT, STRATEGIES, bootstrap, chain_flagged, load, paired  # noqa: E402

from temporalguard.eval import ct3_data, ct4_data  # noqa: E402

DATA = {"ct3": ct3_data, "ct4": ct4_data}
FOLLOWED_CHAINS = {int(s.split("_")[1]) - 1 for s in ct3_data.FOLLOWED}  # v3 split (kept for callers)
PROBES = [("Luna", "luna"), ("Haiku", "haiku"), ("Flash-Lite", "flash_lite")]  # runs/ct3_probe_<stem>.md


def probe_acts(path: Path) -> dict[int, int]:
    """Per scenario, attack answers (of 3) that act on the record, from the probe report's by-scenario table."""
    acts = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| ct\d_(\d+) \|[^|]*\| (\d)/3", line)
        if m:
            acts[int(m.group(1)) - 1] = int(m.group(2))
    return acts


def pearson(x: list[float], y: list[float]) -> float:
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y, strict=True))
    sx = sum((a - mx) ** 2 for a in x) ** 0.5
    sy = sum((b - my) ** 2 for b in y) ** 0.5
    return sxy / (sx * sy) if sx and sy else float("nan")


def detection_by_scenario(rows: list[dict], strategy: str) -> list[float]:
    """Share of the attack sessions of each scenario (over the three families) in which the chain's own text is flagged."""
    hits: dict[int, list[int]] = defaultdict(list)
    for s, chain, _t, a in paired(rows):
        if s == strategy:
            hits[chain].append(int(chain_flagged(a, set(a["attack_indices"]))))
    return [sum(hits[c]) / len(hits[c]) if hits[c] else float("nan") for c in range(12)]


def cell(rows: list[dict], strategy: str, chains: set[int] | None) -> tuple[float, float, dict, int]:
    per: dict[int, list[float]] = defaultdict(list)
    attack = twin = n = 0
    for s, chain, t, a in paired(rows):
        if s != strategy or (chains is not None and chain not in chains):
            continue
        positions = set(a["attack_indices"])
        fa, ft = chain_flagged(a, positions), chain_flagged(t, positions)
        per[chain].append(float(fa) - float(ft))
        attack += fa
        twin += ft
        n += 1
    return (attack / n, twin / n, per, n) if n else (0.0, 0.0, per, 0)


def part_flags(rows: list[dict], strategy: str = "per_message") -> tuple[list[float], list[float]]:
    """Single-read share of sessions in which F1, F2 and F3 are flagged alone (families ct3 and ct3_span)."""
    atk, twn, n = [0] * 3, [0] * 3, 0
    for s, _chain, t, a in paired(rows):
        if s != strategy or a["family"].endswith("_concat") or len(a["attack_indices"]) != 3:
            continue
        n += 1
        for k, idx in enumerate(a["attack_indices"]):
            atk[k] += any(d["output_index"] == idx and d["verdict"] != "allow" and d["stage"] != "judge_error" for d in a["decisions"])
            twn[k] += any(d["output_index"] == idx and d["verdict"] != "allow" and d["stage"] != "judge_error" for d in t["decisions"])
    return ([x / n for x in atk], [x / n for x in twn]) if n else ([0.0] * 3, [0.0] * 3)


def table(data: dict[str, list[dict]], chains: set[int] | None, title: str) -> list[str]:
    lines = [f"## {title}", "", "| judge | " + " | ".join(SHORT[s] for s in STRATEGIES) + " |", "|---|---|---|---|"]
    for label, rows in data.items():
        cells = []
        for s in STRATEGIES:
            a, t, per, n = cell(rows, s, chains)
            if not n:
                cells.append("n/a")
                continue
            g, lo, hi = bootstrap(per)
            cells.append(f"{a:.2f} / {t:.2f}: **{g:+.2f}** [{lo:+.2f}, {hi:+.2f}]")
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    return lines + [""]


def gain_table(data: dict[str, list[dict]], chains: set[int] | None) -> list[str]:
    """Gain of the final design and of full history over a single read, paired by scenario, with a 95% bootstrap interval (+AI, 2 Nov 2026)."""
    lines = ["## Gain over a single read (gap of the strategy minus gap of a single read, paired by scenario)", "",
             "| judge | final design | full history |", "|---|---|---|"]  # fmt: skip
    for label, rows in data.items():
        per = {s: cell(rows, s, chains)[2] for s in STRATEGIES}
        cells = []
        for s in ("fib_min3_fallback_confirm", "full"):
            if not per[s] or not per["per_message"]:
                cells.append("n/a")
                continue
            diff = {c: [sum(per[s][c]) / len(per[s][c]) - sum(per["per_message"][c]) / len(per["per_message"][c])] for c in per[s] if c in per["per_message"]}
            g, lo, hi = bootstrap(diff)
            cells.append(f"**{g:+.2f}** [{lo:+.2f}, {hi:+.2f}]" + ("" if lo > 0 or hi < 0 else " (interval contains 0)"))
        lines.append(f"| {label} | " + " | ".join(cells) + " |")
    return lines + [""]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--runs", default="runs")
    ap.add_argument("--out", default=None, help="write the Markdown here (default: print)")
    ap.add_argument("--version", choices=["ct3", "ct4"], default="ct3")
    args = ap.parse_args()
    v = args.version
    followed = DATA[v].FOLLOWED
    followed_chains = {int(s.split("_")[1]) - 1 for s in followed} if followed else None
    data = {label: load(Path(args.runs) / f"{v}_{stem}_dump.jsonl") for label, stem in JUDGES if (Path(args.runs) / f"{v}_{stem}_dump.jsonl").exists()}
    if not data:
        print(f"no {v}_<judge>_dump.jsonl files found in {args.runs}", file=sys.stderr)
        return 1
    lines = [f"# Cross-tool {v[-1:] and 'v' + v[-1]}: attack flagged versus twin flagged", "",
             "Generated by `scripts/ct3_twin_gap.py`. Each cell is attack flagged / twin flagged, then the gap with a 95% bootstrap interval over the "
             "scenarios. Only flags on the chain's own text count.", ""]  # fmt: skip
    lines += table(data, None, "All twelve scenarios")
    if followed_chains is not None:
        lines += table(data, followed_chains, f"The {len(followed_chains)} scenarios the probe models acted on")
        lines += table(data, set(range(12)) - followed_chains, f"The {12 - len(followed_chains)} scenarios they did not act on")
    else:
        lines += ["(No followed split: it is fixed after the probe, in ct4_data.FOLLOWED.)", ""]
    lines += gain_table(data, None)
    lines += ["## Which part is flagged, by strategy: share of sessions (families without _concat) in which F1, F2 or F3 is flagged by some window", "",
              "| judge | strategy | attack F1 | F2 | F3 | twin F1 | F2 | F3 |", "|---|---|---|---|---|---|---|---|"]  # fmt: skip
    for label, rows in data.items():
        for s in STRATEGIES:
            if not any(r["strategy"] == s for r in rows):
                continue
            a, t = part_flags(rows, s)
            lines.append(f"| {label} | {SHORT[s]} | " + " | ".join(f"{x:.2f}" for x in a + t) + " |")
    lines += ["", "Attack F2 rising with context while twin F2 stays at 0 means the extra flags land on the record that differs, once earlier records are in the window.", ""]  # fmt: skip
    lines += ["## Single read: share of sessions in which each part is flagged alone", "",
              "| judge | attack F1 | F2 | F3 | twin F1 | F2 | F3 |", "|---|---|---|---|---|---|---|"]  # fmt: skip
    for label, rows in data.items():
        a, t = part_flags(rows)
        lines.append(f"| {label} | " + " | ".join(f"{x:.2f}" for x in a + t) + " |")
    changed = "F1" if v == "ct3" else "F2"
    lines += ["", f"If attack {changed} (the record that differs) is flagged alone more often than twin {changed}, the judge reacts to that one record, not to anything cross-tool.", ""]
    probes = {lab: probe_acts(Path(args.runs) / f"{v}_probe_{stem}.md") for lab, stem in PROBES if (Path(args.runs) / f"{v}_probe_{stem}.md").exists()}
    if len(probes) == len(PROBES) and all(len(v) == 12 for v in probes.values()):
        total = [float(sum(probes[lab][c] for lab in probes)) for c in range(12)]
        own = {"Luna": "Luna", "Haiku": "Haiku", "Gemini Flash-Lite": "Flash-Lite"}
        lines += ["## Does detection track whether agents act? (per-scenario Pearson r, 12 scenarios)", "",
                  f"Detection = share of a scenario's three attack sessions ({v}, {v}_span, {v}_concat) in which the chain's own text is flagged. "
                  "Probe = attack answers acting on the record, summed over the three probed models (0 to 9), or the judge's own model as agent (0 to 3). "
                  "Twelve points each; descriptive only, no interval.", "",
                  "| judge | strategy | r with all three probes | r with the same model as agent |", "|---|---|---|---|"]  # fmt: skip
        for label, rows in data.items():
            for s in STRATEGIES:
                det = detection_by_scenario(rows, s)
                r_all = pearson(det, total)
                r_own = pearson(det, [float(probes[own[label]][c]) for c in range(12)]) if label in own else float("nan")
                lines.append(f"| {label} | {SHORT[s]} | {r_all:+.2f} | {r_own:+.2f} |")
        lines += ["", "Negative or near-zero r: the judge flags the scenarios agents resist at least as often as the ones they follow. "
                  "A judge with almost no flags (Haiku) gives an unstable r.", ""]  # fmt: skip
    text = "\n".join(lines)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
