# Experiment log

Every experiment in the repository, where its files are, which command produced it and whether the README reports it.
File counts are generated from `runs/` (tables and dumps together). Total spend and the exploratory runs are in `COMMANDS.md` Part 2 I2 and I3.

| Experiment | Judges | Files in `runs/` | Count | Commands | Reported |
|---|---|---|---|---|---|
| Midterm engineered suite | Luna; Haiku (early Haiku 4.5 run) | `real_*` | 3 | Part 2 A | midterm report only |
| Twin designs (three negative results) | Luna, Haiku | `twin*`, `cascade_twin_*` | 8 | Part 2 B | yes (limits) |
| Strategy grid on long sessions | Luna, Haiku | `ref_*` | 10 | Part 2 C | yes (Results 1 to 3) |
| Early-stop ablation, final designs, synthetic benign | Luna, Haiku | `minwin_*`, `final_*`, `def_*`, `benign_*` | 22 | Part 2 D | yes (Results 2) |
| AgentDojo-derived attacks | Luna, Haiku, Gemini | `ad_check_*`, `ad_final_*` | 11 | Part 2 E | yes (Results 1) |
| AgentDojo benign sessions | Luna, Haiku, Gemini | `ad_benign_*` | 12 | Part 2 F | yes (Results 4) |
| Cascades and strong-only baselines | Luna+Sol, Haiku+Sonnet | `ad_cascade_*`, `ad_cheaponly_*`, `ad_solonly_*`, `ad_sonnetonly_*`, `cascade_twin8_*`, `twin8_*` | 22 | Part 2 G | yes (Results 4, 5) |
| Schedule-aware attacker | Luna, Haiku, Gemini | `adaptive_*` | 6 | Part 2 G2 | yes (Results 2) |
| Gate plus cascade pipeline | Luna+Sol, Haiku+Sonnet, Gemini | `ad_pipeline_*`, `*gemini_pipeline*` | 7 | Part 2 G3; Part 5 M | yes (Results 5) |
| Semantic gate | Luna, Haiku | `gate_*` | 16 | Part 2 G4 | yes (Results 6) |
| Gemini evaluations, cascade and Pro-only baseline | Gemini 3.1 Pro, Flash-Lite | `gemini_cascade_*`, `gemini_pro_final*`, `gemini_pro_only*` | 13 | Part 5 J, K, N | listed; results not summarised in the README |
| Cross-tool v1 and v2 (discarded) | Gemini, Luna, Haiku | not in the repository | 0 | `docs/CROSS_TOOL.md` | run and discarded; design could not support a conclusion |
| LogicInception-style attacks, variants A and B | Luna, Haiku, Sonnet, Sol | `liA_openai*`, `liB_openai*`, `liA_claude*`, `liB_claude*`, `li?_sonnet*`, `li?_sol*` | 24 | Part 6.1, 6.3 | yes (Results 7, 8) |
| LogicInception-style chains with benign twins | Luna, Haiku, Sonnet, Sol, Gemini Pro, Flash-Lite | `li?_twin_*` | 24 | Part 6.2 to 6.4 | yes (Results 7, 8) |
| Cross-tool v3 agent-compliance probe | gpt-6-luna, claude-haiku-5-5, gemini-3.1-flash-lite | `ct3_probe_*` | 7 | Part 8.2 | yes (README, Cross-tool v3) |
| Cross-tool v3 cheap-judge runs | Luna, Haiku, Flash-Lite | `ct3_openai_*`, `ct3_claude_*`, `ct3_gemini_flash*` | 6 | Part 8.4, 8.5 | yes, as a diagnostic result (README, Cross-tool v3) |
| Cross-tool v3 strong judges| Sonnet, Gemini Pro (not run) | n/a | 0 | Part 8.4 | no; kept for v4 if useful |
| Cross-tool v4 semantic gate | none (local embedder) | `ct4_gate_calibrate*.txt` | 2 | Part 9.8 | yes (README, limitation) |
| Cross-tool v4 single-read pilot | Luna | `ct4_pilot/*` (summary, table, dump) | 3 | Part 9.2 | yes (README, Cross-tool v4) |
| Cross-tool v4 agent-compliance probe | gpt-6-luna, claude-haiku-5-5, gemini-3.1-flash-lite | `ct4_probe_*` | 6 | Part 9.4 | yes (README, Cross-tool v4) |
| Cross-tool v4 cheap-judge runs | Luna, Haiku, Flash-Lite | `ct4_openai_*`, `ct4_claude_*`, `ct4_gemini_flash*` | 6 | Part 9.5, 9.6 | yes (README, Results 10) |
| Cross-tool v4 strong-judge runs | Sonnet, Sol, Gemini Pro | `ct4_sonnet_*`, `ct4_sol_*`, `ct4_gemini_pro*` | 6 | Part 9.7 | yes (README, Results 10) |
| Twin-gap tables | (analysis of the dumps above) | `li_twin_gap_summary.md`, `ct3_twin_gap_summary.md`, `ct4_twin_gap_summary.md` | 3 | Part 6.5, 8.5, 9.6 | yes |

## Not used in any result

- Exploratory runs on 28 October (about $1.5 of API credit across OpenAI and Anthropic), recorded only in the private shell history.
- `cache_*_old.jsonl`, `cache_anthropic.jsonl` and other superseded caches (git-ignored).

## Tables with judge errors

Across the result tables only six have `err` above 0.00: the Sonnet LogicInception tables (`liA_sonnet_v1`, `liB_sonnet_v1`, `liA_sonnetwin_v1`,
`liB_sonnetwin_v1`, `liA_twin_sonnet_v1`, `liB_twin_sonnet_v1`; 0.001 to 0.004). Sonnet refused four outputs, all on the Slack chain `slack_2`; counting
them as flags or ignoring them changes no figure.

## Reproducibility caveats

- The v3 probe round-1 tables are not in the repository (cache only: `runs/ct3_probe_cache.jsonl`).
- Cross-tool v1 and v2 were run and discarded; their files and generator code are not in the repository (`docs/CROSS_TOOL.md`).
- Gemini models are previews and were run through Google's batch API; the Gemini cost is in `COMMANDS.md` Part 2 I3.
- Judge caches are git-ignored (about 63 MB). A cache-only rerun uses `--max-real-calls 0` and fails on a missing window instead of paying for it.
