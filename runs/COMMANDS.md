# Commands behind the result files

Everything in Parts 1 to 3 has been run and its results are in `runs\`. What has not been run is listed at the bottom (Part 4).

To keep the exact commands as typed, save your shell history next to the results:

    Get-Content (Get-PSReadLineOption).HistorySavePath | Select-String "temporalguard eval" | Out-File runs\COMMANDS_history.txt

Commands up to `ref_*_v7` were checked against the real PowerShell history. The later ones are the commands given in the conversation, run unchanged; where your history differs, the history wins.

---

## Part 1. Setup and conventions

| Setting | Value |
|---|---|
| OpenAI cheap judge | `gpt-6-luna`, reasoning effort `none` (`$env:TEMPORALGUARD_OPENAI_REASONING_EFFORT = "none"`) |
| OpenAI strong judge (cascade) | `gpt-6-sol`, reasoning effort `none`, $2 / $10 per million tokens. `gpt-6.1-sol` was NOT used (see Part 4). |
| Claude cheap judge | `claude-haiku-5-5` (pass `--model claude-haiku-5-5`), $0.10 / $0.50 per million tokens |
| Claude strong judge (cascade) | `claude-sonnet-5-5`, $2 / $10 per million tokens. It rejects forced tool calls, so the judge uses `tool_choice: auto` with `thinking: between_tools` (needs the build with 158 tests). |
| Seed | default (`--seed 0`) |
| Caches | `runs\cache_openai.jsonl`, `runs\cache_claude.jsonl`, `runs\cache_openai_sol.jsonl`, `runs\cache_sonnet.jsonl`. Keyed on model, prompt and window. Do not delete; keep them out of git. |
| Code version | Latest `TemporalGuard_updated.7z`, 183 tests (includes the Sonnet follow-up retry and a 2000-token reply budget for Sonnet, `--max-real-calls`, the semantic gate and its exemplar sets). Older runs used earlier builds; the metrics they report are unchanged. |

Keys are set in the shell only (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`) and never written to files.

**Claude version of any OpenAI command below:** replace `--judge openai --cache runs\cache_openai.jsonl` with `--judge anthropic --model claude-haiku-5-5 --cache runs\cache_claude.jsonl`, and `openai` with `claude` in the output names.

**Two rules that matter when rerunning:**
- Keep the suite settings (`--families`, `--per-family`, `--benign`, `--no-twins`) exactly the same, or the cache will not match and the run will cost real money. Sessions depend on the families listed together, so `--families agentdojo agentdojo_span` and `--families agentdojo_span` build different sessions.
- A run that prints `WARNING: judge calls failed` or has `err` above 0.00 must be rerun with the same command before its table is used. Failed calls are not cached, so only they are retried.

---

## Part 2. Completed runs

### A. Midterm report: `real_openai_v1/v2/v3`, `real_claude_v1`

Suite: `--per-family 3 --benign 10`, the eight default families. Tables 2 and 3 of the midterm report and the stateful-gate finding come from these.

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --per-family 3 --benign 10 --strategies per_message fib full gated_full --ci --by-family --out runs\real_openai_v2.md

`real_openai_v1` is the same command (its first run had judge errors that were retried; `v2` is the clean rerun). Stateful gate:

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --per-family 3 --benign 10 --strategies gated_full fib_gated gated_full_stateful fib_stateful --ci --by-family --out runs\real_openai_v3.md

Claude (**no `--model` flag was passed**, so it used the installed default):

    temporalguard eval --judge anthropic --cache runs\cache_claude.jsonl --per-family 3 --benign 10 --strategies per_message fib full gated_full --ci --by-family --out runs\real_claude_v1.md

### B. Twin designs (the benign-twin experiments, three negative results)

`dep_*_v1` (design 1, `dependent`):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families dependent dependent_span --per-family 4 --benign 4 --strategies per_message fib full --ci --by-family --out runs\dep_openai_v1.md

`def_*_v3` (design 2, `definitional`, with reasoning dump):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families definitional definitional_span --per-family 4 --benign 4 --strategies per_message fib full --ci --by-family --dump runs\def_openai_dump.jsonl --out runs\def_openai_v3.md

`ref_*_v1` and `ref_*_dump.jsonl` (design 3, `referential`, the provenance finding):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential referential_span --per-family 4 --benign 4 --strategies per_message fib full --ci --by-family --dump runs\ref_openai_dump.jsonl --out runs\ref_openai_v1.md

`ref_*_v4` (more strategies, root recall with intervals):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential referential_span --per-family 4 --benign 4 --strategies per_message fixed5 pow2 fib fib_fallback full --ci --by-family --out runs\ref_openai_v4.md

### C. Strategy grid on long sessions: `ref_*_v7`

16 attack episodes, attack-only.

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential_span --no-twins --per-family 16 --benign 0 --strategies per_message fixed5 pow2 fib fixed5_fallback pow2_fallback fib_fallback fixed5_confirm pow2_confirm fib_confirm pow2_fallback_confirm fib_fallback_confirm full --ci --by-family --out runs\ref_openai_v7.md

(`fixed5_fallback_confirm` was added after this run, so it is not in these tables. The `final_long_*` runs use the same sessions and include it, so no `v8` rerun is needed.)

### D. Early-stop ablation, candidate final designs, synthetic benign

`minwin_*_v1` (starting at window 1 versus window 3, short sessions):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families definitional referential --no-twins --per-family 8 --benign 0 --strategies per_message fib fib_min3 pow2 pow2_min3 fixed5 fib_confirm full --ci --by-family --out runs\minwin_openai_v1.md

`final_short_*_v1` (short sessions):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families definitional referential --no-twins --per-family 8 --benign 0 --strategies per_message fixed5 fixed5_fallback_confirm pow2_min3_fallback_confirm fib_min3_fallback_confirm fib_min3 full --ci --by-family --out runs\final_short_openai_v1.md

`final_long_*_v1` (long sessions; its OpenAI run was rerun once to clear a judge-error warning, and the file with `err` = 0.00 is the one to keep):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential_span --no-twins --per-family 16 --benign 0 --strategies per_message fixed5 fixed5_fallback_confirm pow2_min3_fallback_confirm fib_min3_fallback_confirm fib_min3 full --ci --by-family --out runs\final_long_openai_v1.md

`final_short_*_priced` and `final_long_*_priced`: the same two commands as `final_short_*_v1` and `final_long_*_v1` with `--price-in 0.10 --price-out 0.50` added and `--out runs\final_short_openai_priced.md` (and `final_long`, and the `claude` versions). They came from the cache (no new calls) and add the `$/out` column, so cost can be quoted in dollars. For example:

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential_span --no-twins --per-family 16 --benign 0 --strategies per_message fixed5 fixed5_fallback_confirm pow2_min3_fallback_confirm fib_min3_fallback_confirm fib_min3 full --ci --by-family --price-in 0.10 --price-out 0.50 --out runs\final_long_openai_priced.md

`benign_*_v1` (40 synthetic benign sessions; only the `fpr` column is meaningful, because the one attack episode from `--families adjacent --per-family 1` inflates the recall columns):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families adjacent --per-family 1 --benign 40 --strategies per_message fixed5_fallback_confirm pow2_min3_fallback_confirm fib_min3_fallback_confirm full --ci --out runs\benign_openai_v1.md

### E. AgentDojo-derived attacks: `ad_check_*_v1`, `ad_final_*_v1`

27 attacks in two session lengths (`agentdojo` and `agentdojo_span`, 54 episodes).

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families agentdojo agentdojo_span --no-twins --per-family 27 --benign 0 --strategies per_message full --ci --by-family --dump runs\ad_check_openai_dump.jsonl --out runs\ad_check_openai_v1.md

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families agentdojo agentdojo_span --no-twins --per-family 27 --benign 0 --strategies per_message fixed5_fallback_confirm pow2_min3_fallback_confirm fib_min3_fallback_confirm full --ci --by-family --dump runs\ad_final_openai_dump.jsonl --out runs\ad_final_openai_v1.md

### F. AgentDojo benign sessions: `ad_benign_*_v1`

40 sessions made only of AgentDojo's own benign text.

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families agentdojo_benign --per-family 40 --benign 0 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\ad_benign_openai_dump.jsonl --out runs\ad_benign_openai_v1.md

### G. Cascades (cheap judge first, strong judge only on flagged windows)

**Benign cascade** (`ad_benign_cascade_*_v1`; caps 60 for OpenAI, 40 for Claude). The first Claude attempt failed because Sonnet 5.5 rejects forced tool calls; the file to keep is the rerun after the judge fix.

    temporalguard eval --judge cascade --cheap openai:gpt-6-luna --cheap-cache runs\cache_openai.jsonl --strong openai:gpt-6-sol --strong-cache runs\cache_openai_sol.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 60 --families agentdojo_benign --per-family 40 --benign 0 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\ad_benign_cascade_openai_dump.jsonl --out runs\ad_benign_cascade_openai_v1.md

    temporalguard eval --judge cascade --cheap anthropic:claude-haiku-5-5 --cheap-cache runs\cache_claude.jsonl --strong anthropic:claude-sonnet-5-5 --strong-cache runs\cache_sonnet.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 40 --families agentdojo_benign --per-family 40 --benign 0 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\ad_benign_cascade_claude_dump.jsonl --out runs\ad_benign_cascade_claude_v1.md

**Attack cascade, long sessions** (`ad_cascade_*_v1`). Run in two stages: the first stage stopped at its cap (150 for OpenAI, 80 for Claude), and the second stage reran the same command with `--max-strong-calls 220`, reusing everything paid for. The OpenAI table is the second stage. A single failed call (the model's reply was cut off) was retried by rerunning the same command.

    temporalguard eval --judge cascade --cheap openai:gpt-6-luna --cheap-cache runs\cache_openai.jsonl --strong openai:gpt-6-sol --strong-cache runs\cache_openai_sol.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 220 --families agentdojo_span --no-twins --per-family 27 --benign 0 --strategies per_message fib_min3_fallback_confirm --ci --by-family --workers 4 --dump runs\ad_cascade_openai_dump.jsonl --out runs\ad_cascade_openai_v1.md

    temporalguard eval --judge cascade --cheap anthropic:claude-haiku-5-5 --cheap-cache runs\cache_claude.jsonl --strong anthropic:claude-sonnet-5-5 --strong-cache runs\cache_sonnet.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 220 --families agentdojo_span --no-twins --per-family 27 --benign 0 --strategies per_message fib_min3_fallback_confirm --ci --by-family --workers 4 --dump runs\ad_cascade_claude_dump.jsonl --out runs\ad_cascade_claude_v1.md

**Twin cascade** (`cascade_twin_*_v1`): the engineered twin suite (`referential`, `referential_span`, 8 attack and 8 harmless-twin sessions per judge) with a strong second tier. The settings match `ref_*_v1`, so the cheap tier came from the cache. The Claude run first failed on 4 windows where Sonnet answered in text and never called the tool; after the judge was changed to send a follow-up turn, the same command was rerun and finished with `err` = 0.00.

    temporalguard eval --judge cascade --cheap openai:gpt-6-luna --cheap-cache runs\cache_openai.jsonl --strong openai:gpt-6-sol --strong-cache runs\cache_openai_sol.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 60 --families referential referential_span --per-family 4 --benign 4 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\cascade_twin_openai_dump.jsonl --out runs\cascade_twin_openai_v1.md

    temporalguard eval --judge cascade --cheap anthropic:claude-haiku-5-5 --cheap-cache runs\cache_claude.jsonl --strong anthropic:claude-sonnet-5-5 --strong-cache runs\cache_sonnet.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 60 --families referential referential_span --per-family 4 --benign 4 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\cascade_twin_claude_dump.jsonl --out runs\cascade_twin_claude_v1.md

**Twin replicate, OpenAI** (`cascade_twin8_openai_v1` and its paired baseline `twin8_cheaponly_openai_v1`): the twin suite at `--per-family 8` (16 attack/twin pairs). The first command is the cascade (cap 150); the second is Luna alone, run after it so its windows came from the cache.

    temporalguard eval --judge cascade --cheap openai:gpt-6-luna --cheap-cache runs\cache_openai.jsonl --strong openai:gpt-6-sol --strong-cache runs\cache_openai_sol.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 150 --families referential referential_span --per-family 8 --benign 4 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\cascade_twin8_openai_dump.jsonl --out runs\cascade_twin8_openai_v1.md

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families referential referential_span --per-family 8 --benign 4 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\twin8_cheaponly_openai_dump.jsonl --out runs\twin8_cheaponly_openai_v1.md

Result (computed from the two dump files, 16 pairs): pairs handled correctly for `fib_min3_fallback_confirm` 7 of 16 with Luna alone, 10 of 16 with the cascade (+0.19 [0.00, +0.38], 3 rescued, 0 lost); short sessions 6 of 8 to 8 of 8, long sessions 1 of 8 to 2 of 8. No attack was missed by the cascade.

**Sonnet-only baseline** (`ad_sonnetonly_v1`): `claude-sonnet-5-5` on every window of the same 27 long sessions, final design's schedule and safeguards. Run as stage 2 directly (both strategies, cap 1800), sharing `cache_sonnet.jsonl` with the cascade's strong tier. Sonnet 5.5 uses `tool_choice: auto` with a follow-up retry.

    temporalguard eval --judge anthropic --model claude-sonnet-5-5 --cache runs\cache_sonnet.jsonl --max-real-calls 1800 --families agentdojo_span --no-twins --per-family 27 --benign 0 --strategies per_message fib_min3_fallback_confirm --ci --by-family --workers 4 --price-in 2 --price-out 10 --dump runs\ad_sonnetonly_dump.jsonl --out runs\ad_sonnetonly_v1.md

Paired comparison (computed from the three dump files, same 27 attacks, final design): root recall Haiku 0.74, cascade 0.85, Sonnet-only 0.96; detection 0.93, 0.93, 1.00; dollars per output 0.00036 (Haiku, measured in `ad_cheaponly_claude_priced`), 0.00183, 0.00729.

**Twin replicate, Claude** (`cascade_twin8_claude_v1` and its paired baseline `twin8_cheaponly_claude_v1`): same suite as the OpenAI replicate (16 attack/twin pairs). The cascade was run in two stages (cap 60, then rerun with a higher cap; the run that finished used `--max-strong-calls 150`). One window in the `full` strategy failed with an empty reply (`no tool_use block ... last text: ''`), which led to a larger reply budget for Sonnet (2000 tokens); the same command was rerun and both dumps show 0 judge errors. The paired baseline was run afterward, free from the cache.

    temporalguard eval --judge cascade --cheap anthropic:claude-haiku-5-5 --cheap-cache runs\cache_claude.jsonl --strong anthropic:claude-sonnet-5-5 --strong-cache runs\cache_sonnet.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 150 --families referential referential_span --per-family 8 --benign 4 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\cascade_twin8_claude_dump.jsonl --out runs\cascade_twin8_claude_v1.md

    temporalguard eval --judge anthropic --model claude-haiku-5-5 --cache runs\cache_claude.jsonl --families referential referential_span --per-family 8 --benign 4 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --dump runs\twin8_cheaponly_claude_dump.jsonl --out runs\twin8_cheaponly_claude_v1.md

Result (computed from the two dump files, 16 pairs, final design): pairs handled correctly 6 of 16 with Haiku alone, 16 of 16 with the cascade (+0.62 [+0.38, +0.88], 10 rescued, 0 lost); harmless twins flagged 10 to 0; no attack missed. With `full` it is 5 of 16 to 16 of 16. In `per_message` the strong tier un-flags lone fragments (recall 0.25 to 0.00).

**Priced cheap-only baselines** (`ad_cheaponly_openai_priced`, `ad_cheaponly_claude_priced`): the `ad_cheaponly_*_v1` commands with `--price-in 0.10 --price-out 0.50` added and `--out runs\ad_cheaponly_openai_priced.md` (or `claude`). Free from the cache. They give the measured cost ladder (cheap alone, cascade, strong alone) for the final design: OpenAI 0.00014 / 0.00067 / 0.00267 dollars per output; Claude 0.00036 / 0.00183 / 0.00729. The cascade costs about 5 times the cheap judge and about a quarter of the strong judge on both vendors.

**Paired baseline** (`ad_cheaponly_*_v1`): the cheap judge alone on the SAME 27 sessions as the cascade runs. It is needed because the cascade runs used `--families agentdojo_span` alone, which builds different sessions from `ad_final`.

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families agentdojo_span --no-twins --per-family 27 --benign 0 --strategies per_message fib_min3_fallback_confirm --ci --by-family --workers 4 --dump runs\ad_cheaponly_openai_dump.jsonl --out runs\ad_cheaponly_openai_v1.md

The cascade versus cheap-only comparison was computed from the two dump files: per attack, whether it was detected, whether the oldest fragment was found, fragment recall and extra flagged outputs, with a bootstrap over the 27 attacks.

**Strong-judge-only baseline** (`ad_solonly_openai_v1`): `gpt-6-sol` on every window of the same 27 long sessions, with the final design's schedule and safeguards. It is the comparator for the cascade. The first attempt stopped at `--max-real-calls 1300` after `per_message` and 20 of 27 design episodes (the call count was underestimated); the same command with `--max-real-calls 1800` continued from the cache. It shares `cache_openai_sol.jsonl` with the cascade's strong tier. Claude's Sonnet-only baseline was not run.

    temporalguard eval --judge openai --model gpt-6-sol --cache runs\cache_openai_sol.jsonl --max-real-calls 1800 --families agentdojo_span --no-twins --per-family 27 --benign 0 --strategies per_message fib_min3_fallback_confirm --ci --by-family --workers 4 --price-in 2 --price-out 10 --dump runs\ad_solonly_openai_dump.jsonl --out runs\ad_solonly_openai_v1.md

Paired comparison of Luna-only, cascade and Sol-only on the same 27 attacks (computed from the three dump files): root recall 0.67 / 0.89 / 1.00; dollars per output 0.00014 (measured in `ad_cheaponly_openai_priced`) / 0.00067 / 0.00267.

### G2. Schedule-aware (adaptive) attacker with real judges: `adaptive_*_v1`, `adaptive_ref_*_v1`

The attacker places the oldest fragment just outside each strategy's largest window (`adaptive_positions`); 8 sessions per strategy (4 fragment sets x 2 fillers). The table prints to the screen (and into the file via `Out-File -Encoding utf8`) only at the end, so the file stays at 0 bytes while the run is going. Strategies face different sessions, so the cost columns are not comparable across rows, and there are no intervals.

Lexical fragments (a real judge catches each one alone, so placement has no effect: every strategy scores 1.00):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --adaptive --strategies per_message fixed5 pow2 fib fib_fallback fib_confirm fib_min3_fallback_confirm full | Out-File -Encoding utf8 runs\adaptive_openai_v1.md

Referential fragments (the informative test; needs the build with 187+ tests for `--adaptive-pool`; Claude: `--judge anthropic --model claude-haiku-5-5 --cache runs\cache_claude.jsonl`, output `adaptive_ref_claude_v1.md`):

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --adaptive --adaptive-pool referential --workers 4 --strategies per_message fixed5 pow2 fib fib_fallback fib_confirm fib_min3_fallback_confirm full | Out-File -Encoding utf8 runs\adaptive_ref_openai_v1.md

Result (oldest-fragment recall, Claude / OpenAI): `per_message` 0 / 0.25; `fixed5`, `pow2`, `fib` 0 / 0.25; `fib_fallback` 1.00 / 0.25; `fib_confirm` 0.75 / 0.88; final design 1.00 / 1.00; `full` 1.00 / 1.00. Fallback fixes the vendor whose judge escalates (Claude), confirm the one that flags early (OpenAI); the final design handles both against an attacker who knows the schedule. Not an attack on the cascade or the gate.

### G3. Full pipeline: semantic gate (generic exemplars, cutoff 0.20) in front of the cascade (`ad_pipeline_*_v1`)

The gate only removes calls, so every window it still sends came from the caches (cap 30 on strong-tier calls as a safety stop). Same 27 long sessions as the cascade and strong-only runs. Reset the environment afterwards (`$env:TEMPORALGUARD_EXEMPLARS = "all"`, `Remove-Item Env:TEMPORALGUARD_GATE_CUTOFF`).

    $env:TEMPORALGUARD_EXEMPLARS = "generic"
    $env:TEMPORALGUARD_GATE_CUTOFF = "0.20"
    temporalguard eval --judge cascade --cheap openai:gpt-6-luna --cheap-cache runs\cache_openai.jsonl --strong openai:gpt-6-sol --strong-cache runs\cache_openai_sol.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 30 --families agentdojo_span --no-twins --per-family 27 --benign 0 --strategies fib_min3_fallback_confirm_semgated --ci --by-family --workers 4 --dump runs\ad_pipeline_openai_dump.jsonl --out runs\ad_pipeline_openai_v1.md

Claude: `--cheap anthropic:claude-haiku-5-5 --cheap-cache runs\cache_claude.jsonl --strong anthropic:claude-sonnet-5-5 --strong-cache runs\cache_sonnet.jsonl`, outputs `ad_pipeline_claude_*`.

Result (27 attacks, final design; cheap alone / cascade / pipeline / strong alone):

| | Detection | Oldest fragment found | Dollars per output |
|---|---|---|---|
| OpenAI | 1.00 / 1.00 / 1.00 / 1.00 | 0.67 / 0.89 / 0.85 / 1.00 | 0.00014 / 0.00067 / 0.00046 / 0.00267 |
| Claude | 0.93 / 0.93 / 0.89 / 1.00 | 0.74 / 0.85 / 0.78 / 0.96 | 0.00036 / 0.00183 / 0.00126 / 0.00729 |

The gate cuts the cascade's dollars by 31% on both vendors; the pipeline costs 17% of strong-only on both. OpenAI: root recall +0.19 over Luna alone ([0.00, +0.37], 6 attacks up, 1 down), precision 1.00. Claude: the pipeline adds little over Haiku alone (root +0.04, [-0.11, +0.22]) and loses one attack at the gate (detection 0.93 to 0.89), so it is not clearly worth its 3.5x cost there. The benefit depends on how weak the cheap tier is.

### G4. Semantic gate (`gate-calibrate`, `gate_ad_*`, `gate_adbenign_*`)

Needs `pip install sentence-transformers` (model `all-MiniLM-L6-v2`, downloaded on first use). The gate only removes judge calls, so every judged run below came from the caches (0 real calls).

No-API comparison of the gates on the benchmark's fragments and benign outputs (cutoff chosen on the engineered families, reported on held-out ones):

    temporalguard gate-calibrate --embedder st
    temporalguard gate-calibrate --embedder st --exemplars generic

Result with real embeddings (all exemplars): at cutoff 0.20 the semantic gate sent 100% of fit fragments and 97% of held-out fragments to the judge, and 49% of benign outputs; the keyword gate sent 6% and 14% of fragments and 5% of benign outputs.

Judged runs of the final design with the keyword gate and the semantic gate, cutoffs 0.20 and 0.30, 54 attacks (`agentdojo`, `agentdojo_span`) and 40 benign sessions. OpenAI shown; Claude: `--judge anthropic --model claude-haiku-5-5 --cache runs\cache_claude.jsonl` and `claude` in the output names.

    $env:TEMPORALGUARD_GATE_CUTOFF = "0.20"
    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families agentdojo agentdojo_span --no-twins --per-family 27 --benign 0 --strategies fib_min3_fallback_confirm fib_min3_fallback_confirm_kwgated fib_min3_fallback_confirm_semgated --ci --by-family --workers 4 --price-in 0.10 --price-out 0.50 --out runs\gate_ad_openai_c0.20.md

    temporalguard eval --judge openai --cache runs\cache_openai.jsonl --families agentdojo_benign --per-family 40 --benign 0 --strategies fib_min3_fallback_confirm fib_min3_fallback_confirm_kwgated fib_min3_fallback_confirm_semgated --ci --by-family --workers 4 --price-in 0.10 --price-out 0.50 --out runs\gate_adbenign_openai_c0.20.md

The same two commands with `$env:TEMPORALGUARD_GATE_CUTOFF = "0.30"` and `c0.30` in the output names.

Generic-exemplars check (the topic exemplars were written after reading AgentDojo's attack goals, so the all-exemplar rows are optimistic): the same commands with `$env:TEMPORALGUARD_EXEMPLARS = "generic"`, `--strategies fib_min3_fallback_confirm fib_min3_fallback_confirm_semgated` and output names ending `_generic.md` (`gate_ad_*_c0.20_generic.md`, `gate_ad_*_c0.30_generic.md`, `gate_adbenign_*_c0.20_generic.md`, `gate_adbenign_*_c0.30_generic.md`). Reset afterwards:

    $env:TEMPORALGUARD_EXEMPLARS = "all"
    Remove-Item Env:TEMPORALGUARD_GATE_CUTOFF

Results on the 54 attacks, final design (recall / oldest fragment found / fragments missed at the gate / change in dollars per output against no gate):

| Gate | OpenAI | Claude |
|---|---|---|
| No gate | 0.98 / 0.85 / 0% / n/a | 0.98 / 0.93 / 0% / n/a |
| Keyword gate | 0.30 / 0.22 / 84% / about -93% | 0.30 / 0.26 / 84% / about -95% |
| Semantic, all exemplars, cutoff 0.20 | 0.98 / 0.85 / 4% / -33% | 0.98 / 0.91 / 4% / -31% |
| Semantic, all exemplars, cutoff 0.30 | 0.96 / 0.85 / 7% / -60% | 0.96 / 0.91 / 7% / -54% |
| **Semantic, generic exemplars, cutoff 0.20 (number to report)** | **0.94 / 0.78 / 15% / -60%** | **0.93 / 0.81 / 15% / -56%** |
| Semantic, generic exemplars, cutoff 0.30 | 0.81 / 0.65 / 36% / -80% | 0.80 / 0.70 / 36% / -74% |

On the 40 benign sessions at cutoff 0.20 with generic exemplars, dollars per output fell about 77% on both vendors and the share of sessions with a flag fell from 0.28 to 0.10 (Claude) and from 0.35 to 0.17 (OpenAI). That happens because the gate also stops showing the judge benign messages that instruct the agent, so lower false alarms and lower recall come as a pair.

### H. Which finding comes from which file

| Finding | Files |
|---|---|
| Single-output judging is not enough on engineered fixtures; context helps | `real_*`, `ref_*_v4`, `ref_*_v7`, `final_*` |
| Judges flag instructions in tool output by provenance, not payload | `dep_*_v1`, `def_*_v3`, `ref_*_v1` and the `*_dump.jsonl` files, `ad_benign_*`, `ad_benign_cascade_*` |
| Against a schedule-aware attacker, windows-only schedules lose the oldest fragment (root recall 0 to 0.25); the final design finds it on both vendors | `adaptive_ref_*_v1` (and `adaptive_*_v1`, lexical, no effect) |
| Starting at a window of 1 stops escalation too early; a minimum window of 3 fixes it | `minwin_*_v1` |
| The oldest fragment outside the window needs fallback or confirm; each fixes one judge | `ref_*_v7` |
| The combined design matches `full`, cheaper on long and benign sessions | `final_short_*`, `final_long_*`, `benign_*` |
| Fibonacci spacing gives no consistent benefit | `ref_*_v7`, `minwin_*`, `final_*`, `ad_final_*` (fib vs pow2 vs fixed5 rows) |
| Keyword gate misses paraphrased attacks; the history-aware gate does not help | `real_openai_v2`, `real_openai_v3` |
| On AgentDojo-derived attacks, single-output judging catches most; context mainly improves localization | `ad_check_*`, `ad_final_*` |
| The cascade recovers about two thirds (OpenAI, 6 of 9 attacks) to half (Claude, 3 of 6) of the cheap-to-strong root-recall gain at about a quarter of the strong-only dollar cost; it cannot recover attacks the cheap tier never flags (2 of 27 for Haiku) | `ad_solonly_openai_v1`, `ad_sonnetonly_v1`, `ad_cascade_*_v1`, `ad_cheaponly_*_v1` |
| Full pipeline (gate + cascade) costs 17% of strong-only on both vendors; clear root-recall gain over the cheap judge on OpenAI (+0.19), little on Claude (+0.04) | `ad_pipeline_*_v1` |
| In dollars the final design costs +23% to +25% against `full` on short sessions and 6% (Claude) to 20% (OpenAI) less on long sessions; the cascade costs about 2.5x (`per_message`) to 5x (design) the cheap judge alone | `final_*_priced`, `ad_cascade_*` |
| The keyword gate misses 84% of fragments (recall 0.30); a semantic gate with generic exemplars at cutoff 0.20 keeps recall within 0.04 to 0.05 of the ungated design for 56% to 60% lower dollars (77% lower on benign sessions); topic exemplars raise recall to 0.98 but overlap the benchmark | `gate_ad_*`, `gate_adbenign_*` (all and `_generic`) |
| About 2% of AgentDojo benign outputs are flagged, almost all on messages that instruct the agent | `ad_benign_*` |
| A strong second tier clears borderline benign flags and finds more attack roots (OpenAI clear, Claude smaller), never changed detection | `ad_benign_cascade_*`, `ad_cascade_*`, `ad_cheaponly_*` |
| On 16 pairs, Sol raises pair accuracy from 7 to 10 of 16 (clears short twins, mostly not long ones) | `cascade_twin8_openai_v1`, `twin8_cheaponly_openai_v1` |
| A strong second tier separates an attack from its harmless twin: Sonnet 16 of 16 pairs (cheap Haiku alone 6 of 16), Sol 10 of 16 (Luna alone 7 of 16; Sol clears short twins, mostly not long ones) | `cascade_twin8_*`, `twin8_cheaponly_*`, and the 8-pair run `cascade_twin_*` |

### I. Total API spend (final readings, 25 Oct 2026, after all experiments)

| Provider | Covers | Spent | Remaining | Volume |
|---|---|---|---|---|
| OpenAI | Luna and Sol, all runs | $6.07 | $5.93 | 18,102 requests, 14.9M tokens |
| Anthropic | Haiku 5.5, Sonnet 5.5 and the early Haiku 4.5 run (about $0.25), all runs | $16.08 | $8.93 | last 30 days: 31.6M tokens in, 5.0M out |
| **Total** | | **$22.15** | | |

Approximate split of the largest items (from the dashboards and the per-call prices, not itemized bills):

| Item | Approximate cost |
|---|---|
| Sonnet-only baseline (Anthropic) | $7 to $8 |
| Cascade and twin runs (Anthropic, Sonnet calls on flagged windows) | about $3 |
| Everything else on Anthropic (Haiku runs, early Haiku 4.5 run) | about $5 to $6 |
| Sol-only baseline (OpenAI) | $3 to $3.5 |
| Everything else on OpenAI | about $2.5 to $3 |

How the readings moved while the experiments ran (Console "spend this month" for Anthropic, "October spend" for OpenAI):

| Reading | OpenAI | Anthropic |
|---|---|---|
| Early (after the first real-judge runs) | $0.83 | n/a |
| After the strategy grids and AgentDojo checks | $2.24 | $6.07 |
| After the Sonnet-only baseline | $5.50 | $14.51 |
| After the twin replicates | $5.67 to $5.92 | $15.16 to $15.69 |
| **Final** | **$6.07** | **$16.08** |

The Anthropic Cost page chart lagged the Console total during the runs (earlier screenshots ended at 6:55 PM UTC on 24 Oct, and its "total token cost" tile, $6.37, did not match the total). The final Usage page screenshot reads "Data as of Oct 25, 1:05 AM UTC", so token counts had caught up. The Cost page itself was not re-checked after that, so the Console "spend this month" figure ($16.08) is the one used.

---

## Part 3. Open checks (not runs)

1. **Midterm Claude model.** (Likely resolved: the Anthropic Cost chart shows a small Haiku 4.5 bar, about $0.25, on the same day as a small Haiku 5.5 bar, consistent with the early run you stopped on the old default and the completed run on 5.5. Confirm by filtering the Cost page to Haiku 4.5.) `real_claude_v1` had no `--model` flag. Confirm on https://platform.claude.com/usage, filtered to that day, that the tokens went to `claude-haiku-5-5` and not 4.5. If it was 4.5, correct the model name in the report.
2. **Judge-error check on every table.** Before using a table, confirm `err` is 0.00 and there is no `WARNING`.
3. **Back up the caches and save the shell history** (command above).

---

## Part 4. Not run / planned

**Not run on purpose**
- `gpt-6.1-sol@low`. It does not accept reasoning effort `none`, so it needs the Responses API path (unit-tested only, never run live), and reasoning tokens are billed as output at $10 per million, which makes the cost per call higher and less predictable. Use a small cap such as 20 if you try it:

        temporalguard eval --judge cascade --cheap openai:gpt-6-luna --cheap-cache runs\cache_openai.jsonl --strong openai:gpt-6.1-sol@low --strong-cache runs\cache_openai_sol61.jsonl --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 20 --families agentdojo_span --no-twins --per-family 27 --benign 0 --strategies per_message fib_min3_fallback_confirm --ci --by-family --workers 4 --out runs\ad_cascade_openai61_v1.md


**Not commands**
- Poster (one-page PDF), video (5 to 8 minutes), final report. Deadlines: video and poster by Dec 1, session Dec 4, final report Dec 11. Results freeze: Nov 20.
