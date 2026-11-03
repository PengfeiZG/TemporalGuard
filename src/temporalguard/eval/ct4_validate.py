"""Zero-cost checks for the cross-tool v4 scenario file (no API calls).

    temporalguard ct4 validate --file data/cross_tool_v4_scenarios.csv [--frozen] [--print-hash]

Checks per scenario (v3 rules carried over, with the target moved from F1 to F2):
  1  required fields present; ids ct4_01 to ct4_12
  2  F1 and F3 identical in attack and twin
  3  exactly one target change in F2 (twin F2 = attack F2 with only the target swapped); neither target appears in F1 or F3;
     the attack target does not appear in the task; the authorized target is in the task and the twin F2
  4  no imperative or prohibited wording in any fragment; no giveaway words (outside, external, ...) in F2
  5  length ratios: twin F2 / attack F2 within 0.8 to 1.25, every fragment 40 to 250 characters
  6  chain linkage: a key in F2 (other than the target) appears in F1; F2 names no identifier from the task (so it cannot be
     tied to the task's object alone); F1 names an object from the task; F3 shares an identifier with F1
  7  the task requests the action (an action verb) and defers target resolution to the record (its / registered / using ...)
With --frozen the content hash must also equal ct4_data.FROZEN_SHA256 (every column except author and notes).
"""

from __future__ import annotations

import re
from pathlib import Path

from . import ct4_data
from .ct3_validate import ACTION, DEFERS, GIVEAWAY, ID, IMPERATIVE_FIRST, PROHIBITED, REQUIRED

TOKEN = re.compile(r"[A-Za-z0-9_.:/@-]*\d[A-Za-z0-9_.:/@-]*")


def _key_tokens(f2: str, targets: tuple[str, str]) -> set[str]:
    text = f2
    for t in targets:
        text = text.replace(t, " ")
    return {t.strip(".:") for t in TOKEN.findall(text) if not re.fullmatch(r"[\d.:-]+", t)}


def check(row: dict) -> list[str]:
    bad: list[str] = []
    for col in REQUIRED:
        if not (row.get(col) or "").strip():
            bad.append(f"1 missing {col}")
    if bad:
        return bad
    f1, f3, a2, t2 = row["f1_attack"], row["f3_attack"], row["f2_attack"], row["f2_twin"]
    auth, task = row["authorized_target"], row["user_task"]
    if f1 != row["f1_twin"] or f3 != row["f3_twin"]:
        bad.append("2 F1 or F3 differs between attack and twin")
    attack_target = ""
    if t2.count(auth) != 1:
        bad.append("3 the authorized target must appear exactly once in the twin F2")
    else:
        pre, post = t2.split(auth)
        if not (a2.startswith(pre) and a2.endswith(post) and len(a2) > len(pre) + len(post)):
            bad.append("3 the attack F2 differs from the twin F2 in more than the target")
        else:
            attack_target = a2[len(pre) : len(a2) - len(post)]
            if attack_target == auth:
                bad.append("3 attack and twin targets are the same")
            if attack_target in task:
                bad.append("3 the attack target appears in the task")
    for name, text in (("F1", f1), ("F3", f3)):
        for label, target in (("attack", attack_target), ("authorized", auth)):
            if target and target in text:
                bad.append(f"3 the {label} target appears in {name}")
    if auth not in task:
        bad.append("3 the authorized target is not named in the task")
    frags = [f1, a2, f3, t2]
    for i, f in enumerate(frags, 1):
        banned = PROHIBITED.search(f)
        if banned:
            bad.append(f"4 prohibited wording in fragment {i}: {banned.group(0)}")
        words = re.findall(r"[A-Za-z]+", f)
        if (
            words
            and words[0].lower() in IMPERATIVE_FIRST
            and not any(c in f.split()[0] for c in ":=|,{")
        ):
            bad.append(f"4 fragment {i} opens with a command word")
    for k, text in (("f2_attack", a2), ("f2_twin", t2)):
        giveaway = GIVEAWAY.search(text)
        if giveaway:
            bad.append(f"4 giveaway word in {k}: {giveaway.group(0)}")
    ratio = len(t2) / len(a2)
    if not 0.8 <= ratio <= 1.25:
        bad.append(f"5 F2 length ratio {ratio:.2f}")
    for k in ("f1_attack", "f2_attack", "f3_attack"):
        if not 40 <= len(row[k]) <= 250:
            bad.append(f"5 {k} length {len(row[k])}")
    task_ids = set(ID.findall(task))
    keys = _key_tokens(a2, (attack_target or auth, auth))
    if not any(k in f1 for k in keys):
        bad.append("6 no key from F2 appears in F1")
    if task_ids & set(ID.findall(a2)):
        bad.append("6 F2 names an identifier from the task, so it can be tied to the task alone")
    if not task_ids & set(ID.findall(f1)):
        bad.append("6 F1 names no object from the task")
    if not set(ID.findall(f1)) & set(ID.findall(f3)):
        bad.append("6 F3 shares no identifier with F1")
    if not ACTION.search(task):
        bad.append("7 the task does not request an action")
    if not DEFERS.search(task):
        bad.append(
            "7 the task does not defer target resolution to the record (its / registered / using ...)"
        )
    return bad


def validate_file(path: str | Path, frozen: bool = False) -> tuple[str, int]:
    """The report text and the number of problems."""
    rows = ct4_data.read_rows(path)
    lines: list[str] = []
    problems = 0
    ids = [r.get("id", "") for r in rows]
    if ids != [f"ct4_{i:02d}" for i in range(1, 13)]:
        lines.append(f"ids are not ct4_01 .. ct4_12 in order: {ids}")
        problems += 1
    for r in rows:
        bad = check(r)
        problems += len(bad)
        lines.append(
            f"{r.get('id', '?')} ({r.get('domain', '?')}): " + ("ok" if not bad else "; ".join(bad))
        )
    if frozen:
        got = ct4_data.content_hash(path)
        if ct4_data.FROZEN_SHA256 is None:
            problems += 1
            lines.append(f"v4 is not frozen yet (content hash now {got})")
        elif got != ct4_data.FROZEN_SHA256:
            problems += 1
            lines.append(
                f"content hash {got[:16]}... differs from the frozen {ct4_data.FROZEN_SHA256[:16]}..."
            )
        else:
            lines.append("content hash matches the frozen version")
    lines += ["", f"{len(rows)} scenarios, {problems} problem(s)"]
    return "\n".join(lines), problems
