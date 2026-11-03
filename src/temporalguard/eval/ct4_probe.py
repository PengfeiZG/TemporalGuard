"""Agent-compliance probe for cross-tool v4: the v3 probe (eval/ct3_probe.py) run on the v4 file.

    temporalguard ct4 probe --provider openai --model gpt-6-luna --dry-run
    temporalguard ct4 probe --provider openai --model gpt-6-luna --out runs/ct4_probe_luna.md --dump runs/ct4_probe_luna.jsonl
    temporalguard ct4 probe --rescore runs/ct4_probe_luna.jsonl --out runs/ct4_probe_luna.md     (no API calls)

The prompt, scoring and report are the v3 ones; only the scenario file, the default answer cache
(runs/cache_ct4_probe.jsonl, git-ignored) and the changed part (F2 instead of F1) differ.
"""

from __future__ import annotations

from . import ct3_probe, ct4_data


def main(argv: list[str] | None = None) -> int:
    return ct3_probe.main(argv, data=ct4_data, name="ct4")
