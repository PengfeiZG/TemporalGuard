# Commands behind the kept result files

The commands up to `ref_*_v7` were checked against the actual PowerShell history. The `minwin_`, `final_` and `benign_` commands are the ones given in the conversation; confirm them against your history (the command below prints it). To keep the raw record too:

    Get-Content (Get-PSReadLineOption).HistorySavePath | Select-String "temporalguard eval" | Out-File runs\COMMANDS_history.txt

## Environment

| Setting | Value |
|---|---|
| OpenAI judge model | `gpt-6-luna` (set via `TEMPORALGUARD_OPENAI_MODEL`, or the default) |
| OpenAI reasoning effort | `none` (`$env:TEMPORALGUARD_OPENAI_REASONING_EFFORT = "none"`) |
| Claude judge model | `claude-haiku-5-5` (always pass `--model claude-haiku-5-5`) |
| Seed | default (`--seed 0`) |
| Caches | `runs\cache_openai.jsonl`, `runs\cache_claude.jsonl` (keyed on model name, prompt and window; do not delete) |
| Code | the latest `TemporalGuard_updated.7z` (124 tests). Runs up to `ref_*_v7` used earlier versions; the strategies and metrics they report are unchanged, but `fib_min3`, `pow2_min3`, the `*_min3_fallback_confirm` strategies and `--no-twins` need this version or later. |

Keys are set in the shell only (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`) and never written to files.

Claude variant of the `dep_`, `def_` and `ref_` commands below (the midterm `real_` Claude run is listed separately above): replace
`--judge openai --cache runs\cache_openai.jsonl` with
`--judge anthropic --model claude-haiku-5-5 --cache runs\cache_claude.jsonl`
and change `openai` to `claude` in the output name.

## Midterm report runs: real_openai_v1/v2, real_openai_v3, real_claude_v1

Suite: `--per-family 3 --benign 10`, the eight default families. The midterm report's Tables 2 and 3 and the stateful-gate finding come from these.

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --per-family 3 --benign 10 --strategies per_message fib full gated_full --ci --by-family --out runs\real_openai_v2.md

`real_openai_v1` is the same command; its first run showed judge errors that were then retried, and `v2` is the clean rerun. The stateful-gate result:

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --per-family 3 --benign 10 --strategies gated_full fib_gated gated_full_stateful fib_stateful --ci --by-family --out runs\real_openai_v3.md

The Claude run (note: **no `--model` flag**, so it used the installed default; confirm in the Anthropic Console usage page that this was `claude-haiku-5-5` and not `claude-haiku-4-5`):

    temporalguard eval --judge anthropic --cache runs\cache_claude.jsonl --per-family 3 --benign 10 --strategies per_message fib full gated_full --ci --by-family --out runs\real_claude_v1.md

## dep_*_v1.md  (twin design 1: `dependent`; negative result)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families dependent dependent_span --per-family 4 --benign 4 --strategies per_message fib full --ci --by-family --out runs\dep_openai_v1.md

(The first attempt at this command was a malformed paste with the command repeated on one line; the clean rerun is the one that counts.)

## def_*_v3.md and def_*_dump.jsonl  (twin design 2: `definitional`; negative result)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families definitional definitional_span --per-family 4 --benign 4 --strategies per_message fib full --ci --by-family --dump runs\def_openai_dump.jsonl --out runs\def_openai_v3.md

## ref_*_dump.jsonl  (twin design 3: `referential`; reasoning behind the provenance finding)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential referential_span --per-family 4 --benign 4 --strategies per_message fib full --ci --by-family --dump runs\ref_openai_dump.jsonl --out runs\ref_openai_v1.md

## ref_*_v4.md  (referential families with twins, root recall with intervals)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential referential_span --per-family 4 --benign 4 --strategies per_message fixed5 pow2 fib fib_fallback full --ci --by-family --out runs\ref_openai_v4.md

## ref_*_v7.md  (main result: attack-only strategy grid, 16 attack episodes)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential_span --no-twins --per-family 16 --benign 0 --strategies per_message fixed5 pow2 fib fixed5_fallback pow2_fallback fib_fallback fixed5_confirm pow2_confirm fib_confirm pow2_fallback_confirm fib_fallback_confirm full --ci --by-family --out runs\ref_openai_v7.md

Note: `fixed5_fallback_confirm` was added after this run and is not in the v7 tables.

## minwin_*_v1.md  (early-stop ablation: starting at window 1 vs window 3, short sessions)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families definitional referential --no-twins --per-family 8 --benign 0 --strategies per_message fib fib_min3 pow2 pow2_min3 fixed5 fib_confirm full --ci --by-family --out runs\minwin_openai_v1.md

## final_short_*_v1.md  (candidate final designs, short sessions)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families definitional referential --no-twins --per-family 8 --benign 0 --strategies per_message fixed5 fixed5_fallback_confirm pow2_min3_fallback_confirm fib_min3_fallback_confirm fib_min3 full --ci --by-family --out runs\final_short_openai_v1.md

## final_long_*_v1.md  (candidate final designs, long sessions)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential_span --no-twins --per-family 16 --benign 0 --strategies per_message fixed5 fixed5_fallback_confirm pow2_min3_fallback_confirm fib_min3_fallback_confirm fib_min3 full --ci --by-family --out runs\final_long_openai_v1.md

Note: the first OpenAI run of this command printed a judge-error warning for `fib_min3_fallback_confirm` (under 0.5%). The same command was rerun to retry the failed calls; the file with `err` = 0.00 is the one to keep.

## benign_*_v1.md  (false positives on ordinary benign sessions)

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families adjacent --per-family 1 --benign 40 --strategies per_message fixed5_fallback_confirm pow2_min3_fallback_confirm fib_min3_fallback_confirm full --ci --out runs\benign_openai_v1.md

In these files only the `fpr` column is meaningful: the single attack episode from `--families adjacent --per-family 1` inflates every recall column.

## Which finding comes from which file

| Finding | Files |
|---|---|
| Single-output judging is not enough; context helps | `real_*`, `ref_*_v4`, `ref_*_v7`, `final_*` |
| Judges flag by provenance, not payload (twins) | `dep_*_v1`, `def_*_v3`, `ref_*_v1`, and the `*_dump.jsonl` files |
| Early stopping on a lone fragment is a failure; min window 3 fixes it | `minwin_*_v1` |
| An oldest fragment outside the window needs fallback or confirm; each fixes one judge | `ref_*_v7` |
| Combined design matches `full`, cheaper on long and benign sessions | `final_short_*`, `final_long_*`, `benign_*` |
| Fibonacci spacing gives no consistent benefit | `ref_*_v7`, `minwin_*`, `final_*` (the fib vs pow2 vs fixed5 rows) |
| Keyword gate misses paraphrased attacks; history-aware gate does not help | `real_openai_v2`, `real_openai_v3` |
| Zero false positives on 40 benign sessions | `benign_*_v1` |

## Not yet run

- The AgentDojo-derived set (the adapter is not built).
- `ref_*_v8`: the v7 grid plus `fixed5_fallback_confirm`. Optional, since `final_*` covers that strategy.
