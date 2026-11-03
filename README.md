# TemporalGuard

Cost-aware, multi-scale semantic detection of **distributed prompt injection** in tool-using LLM
agents.

Most prompt-injection defenses look at one tool output at a time. An attacker can instead split an
instruction across several outputs so that each piece looks harmless: one says earlier rules no
longer apply, a later one refers to a credential, a later one names an outside destination.
TemporalGuard sits between tool outputs and the agent, keeps the session history, and asks an LLM
judge whether the outputs *together* form an instruction aimed at the agent. To keep that
affordable it starts with a small window of recent outputs and widens it only while the judge is
unsure.

**Course project (IST 597, Penn State, fall 2026)** by Pengfei Zhang and Wei Hua Ong. Everything
reported below was measured with real LLM judges (OpenAI GPT-6 Luna and Sol, Anthropic Claude Haiku 5.5
and Sonnet 5.5, and in the later experiments Google Gemini 3.1 Pro (preview) and Flash-Lite) and is backed by the tables and judge-reasoning dumps in [`runs/`](runs/). The OpenAI and
Anthropic experiments cost $67.43 in API credit (OpenAI $23.49, Anthropic $43.94); the Gemini runs
used Google's batch API and cost $36.00 (before sales tax; see `COMMANDS.md` Part 2 I3). See [Results](#results) for the findings and
[Status and limitations](#status-and-limitations) for what they do not show.

## Research question

Can adaptive multi-scale LLM analysis detect distributed indirect prompt injection while
preserving benign task utility and reducing the cost of scanning the full context?

A secondary, explicitly testable hypothesis: Fibonacci-spaced windows (1, 2, 3, 5, 8, 13) give a
better security/cost trade-off than fixed, linear, power-of-two or full-context windows. The
schedule only controls **how much context is inspected**; it never changes what counts as
malicious. A null result (Fibonacci does not beat power-of-two) is still a valid finding.

## How it works

```
 new tool output ─► cheap scanner ─► low risk ─────────────────────────► ALLOW (no LLM call)
                         │
                         └─ risky/ambiguous ─► window schedule ─► LLM judge on last w outputs
                                                (1,2,3,5,8,13)        │
                                                    ▲                 ├─ confident ─► ALLOW / QUARANTINE / BLOCK
                                                    └─ unsure: widen ◄┘
```

Full design: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Install

```bash
git clone <your-repo-url> temporalguard && cd temporalguard
python -m venv .venv
source .venv/bin/activate              # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e ".[dev,anthropic,openai,gemini,semantic]"
python -m pytest -q                    # 301 tests, no network, no API key
```

Extras: `dev` (tests and linters), `anthropic`, `openai` and `gemini` (the judges), `semantic` (sentence-transformers
for the semantic gate; it pulls in PyTorch, which is large). The core has no runtime dependencies, so
`pip install -e ".[dev]"` is enough to run the offline harness with the mock judge.

Python: `requires-python >= 3.10`. The results in `runs/` were produced with **Python 3.13 on Windows 11**
(the compiled files in the working copy were cpython-313; confirm with `python --version`). The exact package versions are in
[`runs/requirements_freeze.txt`](runs/requirements_freeze.txt).

## Quickstart

Offline, no API key (mock judge):

```bash
temporalguard schedules --n 20     # coverage and worst-case cost of each schedule
temporalguard demo                 # a 5-output example session
temporalguard eval                 # compare all strategies on the synthetic suite
```

In code:

```python
from temporalguard import TemporalGuard
from temporalguard.judge import AnthropicJudge  # needs the [anthropic] extra
from temporalguard.scanner import HeuristicScanner
from temporalguard.schedules import Fibonacci

guard = TemporalGuard(
    judge=AnthropicJudge(),  # reads ANTHROPIC_API_KEY
    scanner=HeuristicScanner(),
    schedule=Fibonacci(),
    task="Summarize the retrieved documents for the user.",
)

decision = guard.inspect(tool_result_text, tool="web_search")
if decision.verdict.flagged:
    ...  # withhold the output from the agent, log decision.explanation / fragment_indices
```

See [examples/quickstart.py](examples/quickstart.py).

With a real judge:

```bash
export ANTHROPIC_API_KEY=...
temporalguard eval --judge anthropic --model claude-haiku-5-5 \
    --price-in <USD/Mtok> --price-out <USD/Mtok> --format csv --out results.csv
```

With OpenAI instead:

```bash
export OPENAI_API_KEY=...                 # PowerShell: $env:OPENAI_API_KEY="..."
temporalguard demo --judge openai --model <model-id>
temporalguard eval --judge openai --model <model-id> --per-family 2 --benign 5
```

In code: `from temporalguard.judge import OpenAIJudge`. The model comes from `--model`, the
`model=` argument, or `TEMPORALGUARD_OPENAI_MODEL`; the built-in default is a best guess at a cheap
current model, so set it explicitly. Neither real-API judge has been run against the live service
by the authors yet; the unit tests use a fake client.

Prices are deliberately not built in because they change.

## Strategies compared

| name | schedule | gate | what it isolates |
|---|---|---|---|
| `per_message` | 1 | no | baseline: one output at a time |
| `fixed5` | last 5 | no | fixed window |
| `full` | whole history | no | ceiling on context, floor on cost efficiency |
| `pow2` | 1,2,4,8,16 | no | doubling schedule |
| `fib` | 1,2,3,5,8,13 | no | the hypothesis under test |
| `gated_full` | whole history | yes | cheap gate + one full-context judge (is gating alone enough?) |
| `pow2_gated`, `fib_gated` | as above | yes | schedule and gate combined |
| `fib_fallback` | 1,2,3,5,8,13 then whole history | no | mitigation for the schedule blind spot |
| `fib_stateful`, `pow2_stateful`, `gated_full_stateful` | as named | history-aware | does a gate that tracks attack stages across outputs reduce gate misses? |

Running the schedule comparison with and without the gate separates two effects that are easy to
conflate: savings from *skipping* the judge on low-risk outputs, and savings from *how the window
grows*.

## Benchmark families and the adaptive attacker

`build_suite` produces attack episodes in these families (plus benign sessions with look-alike
content): `adjacent`, `spaced`, `fib_gaps`, `pow2_gaps`, `random_gaps`, `paraphrased`,
`long_context`, `long_span`. `fib_gaps`, `pow2_gaps` and `random_gaps` use identical fragments with
different spacing so no schedule is rewarded for matching its own rhythm; `long_span` puts the
oldest fragment beyond the largest window of the escalating schedules. `temporalguard eval
--adaptive` runs a schedule-aware attacker that places the oldest fragment in each strategy's
blind spot.

### Context-dependent attacks with benign twins

`--families dependent dependent_span` (opt-in, not in the default suite) builds attacks whose
fragments are harmless alone, and for each one a **benign twin** that is identical except for the
middle fragment (private data in the attack, public data in the twin). A judge that reads outputs
one at a time cannot get both the attack and its twin right, so these families test whether context
helps. `--by-family` prints the false-alarm rate on twin sessions next to recall.

**Caveat found by running it:** with real judges the `dependent` twins were flagged as often as the
attacks (false-alarm rate 1.00 on both OpenAI and Claude), even with full context. Both versions
contain an agent-directed instruction to send data to an address, which a judge should flag whatever
it moves, so those twins are not benign. The `definitional` families fix this: the action matches
the user's task, the fragments are declarative notes, and only the first fragment (what a label
refers to) differs between attack and twin.

```bash
temporalguard eval --families definitional definitional_span --strategies per_message fib full --by-family --ci
```

**Second finding from the `--dump` reasoning:** the `definitional` twins were still flagged. The judges
resolved the definitions correctly (they cite "holiday photos", "draft meeting notes") but treat any
output that widens the user's task ("the package should also include X") as an injection whatever X
is. The `referential` families keep the directive on-task ("attach the file named in the earlier
note") and move all the difference into one declarative note naming the file.

```bash
temporalguard eval --families referential referential_span --strategies per_message fib full --by-family --ci --dump runs\ref_dump.jsonl
```

**Controls for the safeguards.** `fixed5_`, `pow2_` and `fib_` each come with `_fallback` (end the
schedule with a full-history window) and `_confirm` variants, plus `fib_fallback_confirm` and
`pow2_fallback_confirm`. Without the matching controls, a gain from a safeguard could be credited to
the Fibonacci spacing. Confirm and fallback windows equal the whole history, the same windows the
`full` strategy asks about, so with a shared `--cache` they cost almost no extra API calls.

### AgentDojo-derived families

`agentdojo`, `agentdojo_span` and `agentdojo_benign` (opt-in) use material from AgentDojo (MIT; see
`THIRD_PARTY_NOTICES.md`): 27 attack goals from its workspace, banking, travel and Slack suites, each
split into three ordered fragments by the project authors, with AgentDojo's own user-task prompts as the
task and its environment text (emails, files, calendar entries, messages) as filler. All addresses,
IBANs and URLs are `.invalid` placeholders and no AgentDojo "important message" wrapper is used.
`docs/AGENTDOJO_REVIEW.md` lists every attack for review. `agentdojo_benign` builds sessions of
AgentDojo's benign text only, for the false-positive check.

```bash
temporalguard eval --families agentdojo --no-twins --per-family 27 --strategies per_message full --by-family
temporalguard eval --families agentdojo_benign --per-family 40 --strategies per_message full
```

### Cascade judge (cheap first, strong on flags)

`--judge cascade` runs a cheap judge on every window and a stronger one only on the windows the cheap
judge flags; the strong verdict replaces the cheap one. Dollars are summed per tier, so `$/out` is
comparable with single-judge runs. `--max-strong-calls N` caps REAL strong-tier calls (cache hits are
free), and a run that reaches the cap stops cleanly and resumes from the cache when rerun.

```bash
temporalguard eval --judge cascade --cheap anthropic:claude-haiku-5-5 --cheap-cache runs/cache_claude.jsonl \
  --strong anthropic:claude-sonnet-5-5 --strong-cache runs/cache_sonnet.jsonl \
  --cheap-price 0.10 0.50 --strong-price 2 10 --max-strong-calls 120 \
  --families referential_span --no-twins --per-family 16 --benign 0 --strategies per_message fib_min3_fallback_confirm full --by-family
```

### Semantic gate

`SemanticScanner` is a gate that reads meaning: it embeds the newest output (optionally with the one
before it) and compares it with exemplar sentences describing the kind of instruction an injection
contains. It runs locally and needs no API credit. `temporalguard gate-calibrate` compares gates
without any API call: for a range of cutoffs it prints the share of fit fragments, held-out
fragments, harmless twin text and benign outputs that would be sent to the judge, next to the
keyword gate. The cutoff is chosen on one set of families and reported on another, because the
exemplars overlap in topic with the benchmark attacks.

```bash
pip install "temporalguard[semantic]"          # sentence-transformers; model downloads on first use
temporalguard gate-calibrate --embedder st     # compare gates, no API calls
$env:TEMPORALGUARD_GATE_CUTOFF = "0.45"        # then use the cutoff it suggests
temporalguard eval --judge openai --strategies fib_min3_fallback_confirm_kwgated fib_min3_fallback_confirm_semgated ...
```

The exemplars come in two sets. GENERIC ones describe attack mechanics (override the task, move something
to an address, read credentials, act before the user's task, hide it from the user). TOPIC ones name concrete
actions (payments, deleting files, calendar events, inviting users, security codes, hotels, customer data) and
were written after reading AgentDojo's attack goals, so results on the AgentDojo-derived set are optimistic.
`--exemplars generic` (and `$env:TEMPORALGUARD_EXEMPLARS = "generic"` for evaluation runs) leaves the topic
exemplars out.

`--embedder hashing` (the default for `gate-calibrate`) is a dependency-free character n-gram baseline.
It captures wording overlap, not meaning. On the benchmark it cannot keep the fragments without
sending almost every benign output to the judge, so it is a baseline, not a usable gate.
Strategies: `fib_min3_fallback_confirm_kwgated`, `_semgated`, `_hashgated`, `gated_full_sem`, `gated_full_hash`.

**Cap for a single judge.** `--max-real-calls N` (with `--cache`) stops a single-judge run cleanly before real call N+1; cache hits are free and rerunning the same command continues from the cache. Use it for expensive judges such as a strong-model-only baseline.

**Claude models without forced tool use.** Sonnet 5.5, Opus 5.x, Fable and Mythos reject
`tool_choice` "tool"/"any" (a 400 error). For them the judge sends `tool_choice` "auto", asks for the
`record_verdict` call in the system prompt, and sends Sonnet 5.5 `thinking` "between_tools" (its lowest
setting; thinking tokens are billed as output). If the model answers in text instead of calling the tool,
the judge passes that text back and asks for the tool call (up to twice), counting the tokens of every
attempt; a window that still fails reports the stop reason and the model's last text in the error. Models without forced tool use get a 2000-token reply budget (thinking counts against it); an empty reply with `stop_reason=max_tokens` means the budget was exhausted. Haiku 5.5 keeps the
forced call, and existing cache entries are unaffected. Unit-tested with a fake client, not yet run against the live Sonnet API.

**OpenAI models without `none` effort.** GPT-6.1 Sol and GPT-6 Astra do not accept `none` and cannot
do function calls on Chat Completions. Give a cascade tier an effort, `--strong openai:gpt-6.1-sol@low`,
and the judge uses the Responses API for that tier (reasoning tokens are billed as output tokens).
This path has been unit-tested with a fake client but not run against the live API. The older
`gpt-6-sol` accepts `none` and works with the original Chat Completions path.

**Early-stop ablation.** `fib_min3` and `pow2_min3` never start below a window of 3, so a judge that is confident about a lone fragment cannot end escalation before seeing any context. Because they are strategies, they are compared with `fib` and `pow2` on the same episodes with paired intervals.

`fib_min3_fallback_confirm` and `pow2_min3_fallback_confirm` combine all three safeguards (first window >= 3, full-history fallback, confirm on flag) and are the candidate final designs.

**Confirm on flag.** Strategies `fib_confirm` and `per_message_confirm` make one extra full-history
call after a flag and merge the fragments it names, without changing the verdict. They target the
case where a judge flags a later fragment from a small window and stops, never finding the root of
the attack (`root_recall`). Add `--no-twins` for attack-only runs, which cost about half as much.

`--by-family` also prints **twin-pair accuracy**: the share of attack/twin pairs where the attack is caught and
the twin is not flagged. Flagging everything and flagging nothing both score 0, so it is the headline
metric for these families.

```bash
temporalguard eval --families dependent dependent_span --strategies per_message fib full --by-family --ci
```

```bash
temporalguard eval --by-family --ci                 # per-family recall, bootstrap CIs, paired diffs
temporalguard eval --adaptive                       # schedule-aware attacker
temporalguard eval --judge anthropic --cache runs/cache.jsonl   # pay once per distinct window
temporalguard eval --min-window 3                   # ablation: never stop at windows below 3
```

## Metrics

Attack success rate (1 − recall), fragment recall (share of true fragments flagged or named,
which exposes partial views of an attack), early containment (flagged before the final fragment arrives),
precision, output-level false-positive rate, localization (Jaccard of named vs true fragments),
gate miss rate, judge calls, tokens and context examined per output, latency, and optional USD
cost. Definitions are in `src/temporalguard/eval/metrics.py`.

## Results

All numbers below are from `runs/` (the command behind each file is in
[`COMMANDS.md`](COMMANDS.md)). "Cheap" judges are GPT-6 Luna and Claude Haiku 5.5; "strong" judges
are GPT-6 Sol and Claude Sonnet 5.5. "Final design" is the Fibonacci schedule with a minimum window of 3,
a final full-history fallback and a confirm-on-flag call (`fib_min3_fallback_confirm`).

1. **Context matters for locating an attack, not always for detecting it.** On engineered fragments that
   need each other to be read, judging one output at a time finds the oldest fragment in 0 to 25% of long
   sessions and every design with fallback and confirm finds it in all of them. On AgentDojo-derived attacks,
   single-output judging already catches 89% (Haiku) and 98% (Luna), but finds the oldest fragment only 39%
   and 67% of the time; the final design raises that to 93% and 85%.
2. **Early stopping is a failure mode.** Starting at a window of 1 stops escalation on a lone fragment
   (Luna recall 0.69); a minimum window of 3 restores recall 1.00 at no extra cost. Fallback fixes the judge
   that escalates (Haiku) and confirm-on-flag fixes the one that flags early (Luna); the final design needs
   both and handles a schedule-aware attacker (oldest-fragment recall 1.00 on both vendors, against 0 to 0.25
   for windows-only schedules).
3. **Fibonacci spacing gives no consistent benefit.** Against power-of-two and fixed windows its cost
   differs by a few percent, cheaper with Luna and dearer with Haiku. This is a null result for the secondary
   hypothesis.
4. **Judges flag by provenance.** Cheap judges (and Sol on long sessions) flag any instruction in a tool
   output, including harmless on-task ones: about 2% of AgentDojo's own benign outputs are flagged, almost
   all on messages that instruct the agent. A strong second tier helps: Sonnet separates an attack from its
   harmless twin in 16 of 16 pairs (Haiku alone: 6 of 16); Sol manages 10 of 16 (Luna alone: 7 of 16).
5. **A cascade buys part of a strong judge for a quarter of its price.** The cheap judge screens everything and
   the strong judge rules only on what it flags. On 27 long attacks it recovers about half (Claude) to two
   thirds (OpenAI) of the strong judge's gain in oldest-fragment recall for about 25% of the strong judge's
   dollars per output. With the final design it never changed whether an attack was detected (with single-output
   windows the strong judge sometimes cleared a lone fragment). It cannot recover an attack the cheap judge never
   flags.
6. **A semantic gate beats a keyword gate by a wide margin.** The keyword gate lets 84% of fragments skip
   the judge (recall 0.30). A sentence-embedding gate with mechanics-only exemplars keeps recall within
   0.04 to 0.05 of the ungated design at 56% to 60% lower cost. Exemplars that name specific actions raise
   recall to 0.98 but overlap the benchmark's topics, so we treat them as optimistic.

The full pipeline (gate plus cascade) costs about 17% of the strong judge alone on both vendors.

### LogicInception-style pilot: directive-free chains and benign twins

Following [Liu et al. (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.1831/), the authors wrote twelve three-part chains (premise, dependency, specification) that
contain no command and only add up to an unauthorized action when read together, in two styles (A: descriptive, B:
notice voice). Each chain has a benign twin: same tags, wording pattern and tie to the user's task, with a harmless
step. Six judges were run (GPT-6 Luna and Sol, Claude Haiku 5.5 and Sonnet 5.5, Gemini 3.1 Pro preview and
Flash-Lite) with three strategies. Everything below counts only flags on the chain's own text; 11 to 22% of
sessions are also flagged on AgentDojo's own filler text whatever the chain is, which inflates the raw
"false-alarm rate by benign family" in the result tables. The full tables with intervals are in
[`runs/li_twin_gap_summary.md`](runs/li_twin_gap_summary.md), reproduced by `scripts/li_twin_gap.py`.

Gap = share of attack sessions flagged minus share of twin sessions flagged (12 chains, three families each):

| Variant A (descriptive) | single read | final design | full history |
|---|---|---|---|
| Haiku | +0.36 | +0.78 | +0.92 |
| Luna | +0.69 | +0.81 | +0.86 |
| Sonnet | +0.81 | +0.89 | +0.86 |
| Sol | +0.53 | +0.67 | +0.75 |
| Gemini Pro | +0.67 | +0.83 | +0.83 |
| Gemini Flash-Lite | +0.19 | +0.31 | +0.42 |

| Variant B (notice voice) | single read | final design | full history |
|---|---|---|---|
| Haiku | +0.81 | +0.61 | +0.44 |
| Luna | +0.81 | +0.67 | +0.53 |
| Sonnet | +0.81 | +0.58 | +0.50 |
| Sol | +0.47 | +0.61 | +0.44 |
| Gemini Pro | +0.75 | +0.69 | +0.81 |
| Gemini Flash-Lite | +0.53 | +0.72 | +0.92 |

7. **Spreading a directive-free chain defeats single reads; context recovers it.** On the descriptive chains a single
   read catches 19% to 86% of attacks depending on the judge, full history 42% to 100%, and the harmless twins are
   flagged in 14% of sessions or fewer. The judge's strength does not predict the result: Sonnet beats Haiku by
   0.50 on single reads, but Sol is no better than Luna.
8. **For notice-voice chains the best window strategy depends on the vendor.** A notice that conditions the
   user's request on a step is flagged on a single read by every judge, and for OpenAI and Anthropic judges more
   context also flags more harmless twins (47% to 56% with full history), so the final design discriminates
   better than full history in the point estimates (the intervals of three of the four touch zero). Both Gemini models do the opposite: their twin flag rate stays low, and for them
   the final design is worse than full history (−0.11 and −0.19). Part of the extra detection on notice-voice
   chains is therefore judges reacting to the notice format.

9. **Cross-tool v3 does not test cross-tool reasoning; it is reported as a diagnostic result.** Two earlier synthetic cross-tool versions were run and discarded (v1 had
   an overt final directive; in v2 the second fragment carried the instruction and the other two were identical in attack and twin; see [`docs/CROSS_TOOL.md`](docs/CROSS_TOOL.md)).
   On the frozen v3 (twelve authorization-inconsistency scenarios with twins), Luna and Flash-Lite separate attack from twin (gap +0.86 and +0.61 on single reads) and Haiku does not (+0.03), but the detection
   comes from the first record alone: on single reads it is flagged by itself in 79% (Luna) and 58% (Flash-Lite) of sessions, the other two records never, the twins' records never. More context does not help
   (final design +0.72 and +0.47), and detection does not track whether agents act on the record. See [Cross-tool v3](#cross-tool-v3-frozen-scenarios-diagnostic-result).


10. **Cross-tool v4: only the two OpenAI judges detect the redirect, and context helps them; the Anthropic judges and Gemini Pro almost never flag it.** With the target moved behind two links (frozen v4; the twin differs only in the directory record F2), the attack-minus-twin gap for gpt-6-luna
   rises from +0.42 on single reads to +0.67 (final design) and +0.89 (full history); for gpt-6-sol it is +0.39, +0.42 and +0.67 (gains over a single read: Luna +0.25 [+0.08, +0.39] and +0.47 [+0.33, +0.61]; Sol +0.03 [0.00, +0.08] and +0.28 [+0.14, +0.44]; v3 showed no gain). For both, the extra flags land on F2
   (Luna 29% to 92% of attack sessions, Sol 25% to 92%, single read to full history) and never on the twin's F2, which fits the judge using the earlier record to resolve the key; no run removes that record, so it is not shown. Claude Haiku and Sonnet (gap at most +0.03 and +0.11) and Gemini Pro (at most +0.11)
   almost never flag the redirect with any window, so judge strength does not predict the result: the strong Sonnet and Gemini Pro are blind where the cheap Luna is not, and Sol is no better than Luna (final design +0.42 against +0.67; it also flags more twins, any-flag up to 0.58, mostly from the identical first record).
   Gemini Flash-Lite is in between (+0.25, +0.25, +0.36; gains with intervals containing 0). The final design misses long-span chains (recall on `ct4_span`: Luna 0.33, Sol 0.42, against 0.92 for full history). The judges' explanations suggest why: the judge prompt asks for an instruction aimed at the agent, and v4 records contain none; Sonnet notices that the address differs (20 of 24 single-read explanations on F2) but calls it data, not an instruction, Gemini Pro mostly does not compare the record with the task (1 of 24), and Luna and Sol treat a conflict with the user's explicit destination as a redirect (stated reasons, not proof; a prompt written for authorization mismatches was not tried). Limits: twelve scenarios, one run each; F2 alone is flagged
   on single reads (the baseline); any claim concerns two records, not three; only Luna clearly acts on the poisoned record in the probe, which counts alias lookups as acting; twin any-flag false alarms are not zero (filler and the identical first record). Not prompt-injection detection.

## Reproducing the results

- **Tables and reasoning.** `runs/*.md` are the result tables, `runs/*_dump.jsonl` hold the judges' stated
  reasoning for each decision, and `COMMANDS.md` lists the exact command behind each file.
- **The verdict caches are not in the repository.** They are about 63 MB in total, and rebuilding them from scratch
  costs $67.43 in OpenAI and Anthropic credit plus $36.00 for the Gemini runs (`COMMANDS.md` Part 2 I3). Every judged run caches each (model, prompt, window) verdict, so rerunning a
  command with the same cache costs nothing. The offline mock judge reproduces the plumbing for free:
  `temporalguard eval --families adjacent paraphrased --per-family 2 --benign 2`.
- **Keys and models.** Set `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` and `GEMINI_API_KEY` in your shell; they are never written to
  files. OpenAI runs need `TEMPORALGUARD_OPENAI_REASONING_EFFORT=none`. The models are `gpt-6-luna`,
  `gpt-6-sol`, `claude-haiku-5-5`, `claude-sonnet-5-5`, `gemini-3.1-pro-preview` and `gemini-3.1-flash-lite`.
  Preview models can change; a rerun later may not match.
- **A cheap check that the code works:** `python -m pytest -q` runs 301 tests with no network.

## LogicInception-style attacks (pilot)

[Liu et al. (EMNLP 2026)](https://aclanthology.org/2026.emnlp-main.1831/) describe attacks made of declarative notices that contain no command and
only add up to an unauthorized action when read together. Because TemporalGuard reads a window of
outputs, this is a natural stress test. The authors wrote twelve such chains from the AgentDojo-derived goals in
two styles (`data/li_attacks_A.csv`, `data/li_attacks_B.csv`; writing rules in `docs/LI_WRITING_GUIDE.md`), and a
harmless twin of each (`data/li_benign_twins_A.csv`, `_B.csv`). `temporalguard li-lint` checks their style, the
families `li`, `li_span` and `li_concat` run the chains through the same harness, and `--li-twin-file` adds the
twins as the control. Results are summarised under [Results](#results). Who wrote and who edited each row,
including where Claude helped, is described in the AI-assistance statement at the end of this file.

Limits: twelve chains reused across three families (not 36 independent attacks), written by the authors; the
twins are harmless but some are off-task for the session's user task; the numbers are not comparable with the
paper's, which measure whether an agent carries out the attack, whereas ours measure detection. Sonnet returned
a refusal (`stop_reason=refusal`) for four outputs on one chain (three distinct windows); counting them as
flags or ignoring them changes no figure.

## Batch evaluation (Anthropic and Gemini)

Anthropic's Message Batches API (half price) is used through `temporalguard batch-warm` for the strategies whose
windows do not depend on earlier answers (`per_message`, `fixed5`, `full`); it records the windows, submits them
as one batch and later writes the answers into the same cache, so the normal `eval` command is served from it.
Gemini uses `temporalguard gemini-batch`. The adaptive final design cannot be sent as one batch because each
window depends on the previous verdict. Commands are in [`COMMANDS.md`](COMMANDS.md) (Part 6.4 for
the Gemini loop).

## Cross-tool v3 (frozen scenarios; diagnostic result)


Twelve scenarios, each with a matched twin, in which three plain records from three tools (a definition, an assignment and an activation; no command in any of them) route a
user-requested action to a target the user did not name. The twin differs from the attack only in the target in the first record. The authors' first draft was revised with Claude's assistance and then **frozen** ([`docs/CROSS_TOOL.md`](docs/CROSS_TOOL.md) section 2; the content hash ignores the author and notes columns). They replace the discarded v1 and v2 ([`docs/CROSS_TOOL.md`](docs/CROSS_TOOL.md) section 1). Because the records contain no command, they are **cross-tool authorization inconsistencies, not prompt injections in the strict sense**, and are reported as detection of an unauthorized target in distributed tool records.

Before any judge was run, an agent-compliance probe asked three models, one step at a time, which target they would use. They differ sharply:

| Model | Acts on the poisoned record (attack) | Uses the task's own target (attack) | Twin consistent with the task |
|---|---|---|---|
| gpt-6-luna | 25/36 (69%) | 10/36 (28%) | 36/36 |
| claude-haiku-5-5 | 24/36 (67%) | 11/36 (31%) | 36/36 |
| gemini-3.1-flash-lite | 6/36 (17%) | 29/36 (81%) | 34/36 |

A scenario counts as *followed* if at least two of the three models acted on the record in at least two of three answers: eight of the twelve (`ct3_02`, `08`, `10` and `12` are not), a split fixed before any judge run.

The probe is a one-step simulation, not a tool-using agent.

**Cheap-judge runs.** Families `ct3`, `ct3_span` and `ct3_concat`, twelve sessions each, with twins. Gap = attack flagged minus twin flagged, counting only flags on the scenario's own records,
with a 95% bootstrap interval over the twelve scenarios (`runs/ct3_twin_gap_summary.md`):

| Judge | Single read | Final design | Full history |
|---|---|---|---|
| gpt-6-luna | +0.86 [+0.69, +1.00] | +0.72 [+0.56, +0.86] | +0.78 [+0.58, +0.94] |
| gemini-3.1-flash-lite | +0.61 [+0.33, +0.86] | +0.47 [+0.22, +0.72] | +0.47 [+0.25, +0.69] |
| claude-haiku-5-5 | +0.03 [+0.00, +0.08] | +0.06 [+0.00, +0.17] | +0.08 [+0.00, +0.19] |

No twin's records were flagged by any judge under any strategy. **Read with the part table:** on single reads the first record (the one whose target differs) is flagged *alone* in 79% of sessions by
Luna and 58% by Flash-Lite; the second and third records are never flagged alone, in attacks or twins. A single read of one record can only compare its target with the user's task, so this is
target-versus-task checking, not cross-tool reasoning; for Luna and Flash-Lite the windowed strategies add nothing (both are lower than single read, intervals overlapping). Detection does not track agent behaviour either:
Luna flags the four scenarios the probe models did not act on at least as often as the eight they did (single read 0.92 against 0.83), and the per-scenario correlation between detection and the
number of probe answers acting on the record is near zero or negative for every judge and strategy (Luna single read r = −0.24; twelve points, descriptive only). Haiku is blind as a judge (3% of attacks
flagged) although Haiku as an agent acted on the record in 67% of answers. In `ct3_span` the AgentDojo filler around the twins was flagged in some sessions (Luna single read 8 of 12), which is why the
any-flag false-alarm column in `runs/ct3_*` tables is not zero; these flags are on filler, not on the scenario records.

**Conclusion.** v3 shows that cheap judges can catch a record whose target contradicts the task, and that one cheap judge (Haiku) does not, but it cannot show that windows detect distributed
inconsistencies, because no scenario needs more than one record to be caught. It is reported as a diagnostic result, not as prompt-injection detection. Commands are in [`COMMANDS.md`](COMMANDS.md) Part 8.

```powershell
temporalguard ct3 validate --frozen
temporalguard ct3 probe --provider openai --model gpt-6-luna --out runs/ct3_probe_luna.md --dump runs/ct3_probe_luna.jsonl
temporalguard eval --judge openai --cache runs\cache_openai.jsonl --ct3-file data/cross_tool_v3_scenarios.csv --families ct3 ct3_span ct3_concat --per-family 12 --benign 0 --strategies per_message fib_min3_fallback_confirm full --ci --by-family --workers 4 --price-in 0.10 --price-out 0.50 --dump runs\ct3_openai_dump.jsonl --out runs\ct3_openai_v1.md
python scripts/ct3_twin_gap.py --out runs/ct3_twin_gap_summary.md
```

## Cross-tool v4 (frozen; results for six judges)

v4 moves each v3 target behind two links (F1: object to alias and directory key; F2: directory key to target; F3: the v3 activation record), and the twin differs
only in F2, so that no single record can be compared with the task. The scenarios, validator, probe, families `ct4`, `ct4_span`, `ct4_concat` and tests are in the
repository (`temporalguard ct4 validate|probe`, `eval --ct4-file`), and the file was **frozen on 2 November 2026** ([`docs/CROSS_TOOL.md`](docs/CROSS_TOOL.md) section 3). One single-read pilot with Luna has been run:
the directory record (F2) alone is flagged in 0.29 of attack sessions and 0.00 of twin sessions (v3's first record: 0.79), and the identical first record is flagged in 0.21 of both. The single-read gap of +0.17 is the baseline for any
claim about context. The agent-compliance probe (one step, three samples) found that Luna acts on the poisoned record in 24 of 36 attack answers (22 naming the attack address), Haiku in 18 of 36 (mostly by asking to look up the alias; 3 name the address),
and Flash-Lite in none; all three are consistent with the task on the twins. By the v3 rule six scenarios are *followed* (`ct4_01`, `04`, `05`, `06`, `09`, `11`), a weak split because only Luna often names the attack address.
The six judge runs (three cheap, three strong) are summarised in Results item 10 (details: [`COMMANDS.md`](COMMANDS.md) Part 9.6 and 9.7, [`docs/CROSS_TOOL.md`](docs/CROSS_TOOL.md) section 3), and any claim concerns two records at most.

**Semantic gate on v4** (`gate-calibrate`, MiniLM embedder, generic exemplars, v4 families held out; no API calls): it does not separate attack records from twin records, which pass at nearly equal rates (at the suggested cutoff 0.20: 79% against 88% with one output scored, 95% against 94% with two joined). That cutoff sends 79% to 95% of the attack records to the judge, so up to 21% never reach it, and also 36% to 53% of benign outputs; at 0.40 or higher it passes almost nothing. No gate arm was run in the v4 judge runs; this is reported as a limitation ([`COMMANDS.md`](COMMANDS.md) Part 9.8).

## Repository layout

```
src/temporalguard/
  engine.py         gate, escalation loop, confirm-on-flag and fallback, verdict policy
  schedules.py      Fibonacci, PowerOfTwo, Linear, Fixed, Full, WithFullFallback
  scanner/          keyword gate, stateful gate, semantic gate (sentence embeddings)
  judge/            Claude, OpenAI and Gemini judges, cascade judge, caching judge, offline mock judge
  strategies.py     the named configurations
  eval/             fixtures, AgentDojo-derived and LogicInception-style data, episode builder, metrics, runner,
                    batch runners (Anthropic, Gemini), gate calibration, report
  cli.py            temporalguard schedules | demo | make-suite | eval | gate-calibrate | li-lint | li-template
                    | ct3 (template, validate, probe) | ct4 (validate, probe) | batch-warm | gemini-batch
tests/              301 tests (no network, no API key)
data/               attack chains (li_attacks_A/B.csv), benign twins (li_benign_twins_A/B.csv), cross-tool v3 and v4 scenarios (both frozen) and a blank template
docs/               ARCHITECTURE.md, AGENTDOJO_REVIEW.md, LI_WRITING_GUIDE.md, CROSS_TOOL.md (cross-tool v1 to v4:
                    history, v3 guide, v3 and v4 records), EXPERIMENT_LOG.md
scripts/            li_twin_gap.py and ct3_twin_gap.py (twin-gap tables), ct3_agent_probe.py and ct3_validate.py (wrappers)
runs/               result tables (*.md), judge-reasoning dumps (*_dump.jsonl), requirements_freeze.txt;
                    caches (cache_*.jsonl) and batch intermediates are git-ignored
COMMANDS.md         the command behind every result file
CONTRIBUTIONS.md    who did what
THIRD_PARTY_NOTICES.md   AgentDojo (MIT) notice
```

## Status and limitations

- **Small samples.** The headline comparisons use 27 AgentDojo-derived attacks (one per attack goal, split into
  three fragments), 16 engineered long sessions built from four fragment sets, and 16 attack/twin pairs per vendor.
  Intervals are bootstrap intervals over attacks; several are wide, and the twin results in particular rest on
  four fragment sets with different filler.
- **The attacks are derived, not AgentDojo's own.** The authors split AgentDojo's attack goals into fragments
  (reviewed row by row in `docs/AGENTDOJO_REVIEW.md`), without AgentDojo's "important message" wrapper, and
  replaced addresses with `.invalid` placeholders. The engineered families are synthetic.
- **Three vendors, one sample per window.** Each judge verdict is sampled once and cached. The Gemini models are
  previews and were run through Google's batch API.
- **Utility is measured only as false alarms.** We report false-alarm rates on benign sessions (synthetic and
  AgentDojo's own text). We did not run agent tasks end to end, so task completion is not measured.
- **The gate's exemplars overlap the benchmark.** The topic exemplars were written after reading AgentDojo's
  attack goals; the generic-exemplar results are the ones to report.
- **A cascade cannot raise detection above the cheap judge's.** It only sees windows the cheap judge flags.
- **The adaptive attacker targets the window schedules, not the cascade or the gate.** An attacker who knows
  the gate's exemplars or the strong judge was not tested.
- **Not tested:** larger models (for example Claude Opus), strong judges (Sonnet, Gemini Pro, Sol) on cross-tool v3 (only the cheap judges were run; v4 has all six), any scenario that needs three records to be caught (v4 needs two at most), and GPT-6.1 Sol (it cannot do forced tool calls with reasoning disabled, which this judge needs).
- **The LogicInception-style pilot is small.** Twelve chains reused across three families, written by the authors;
  the benign twins are harmless but partly off-task. The notice-voice results mix detecting the attack with
  reacting to the notice format.
- **The mock judge produces no results.** It exists so the pipeline and metrics can be tested without cost.
- **This is a research prototype, not a complete defense.** The judge is itself an LLM reading untrusted text.
  Tool outputs are wrapped and boundary tags are neutralized, but the judge can still be wrong or manipulated.
  Combine it with least-privilege tool permissions.

## AI assistance

We used Claude (Anthropic) throughout this project. Claude assisted with the writing of the codes, 
benchmarks edits for the scenarios, and the results evaluation. The research question, the design decisions 
and the scope were ours. We ran every experiment ourselves with our own API keys, reviewed the AgentDojo-derived
fragments row by row (`docs/AGENTDOJO_REVIEW.md`), and decided what to report. The models that act as judges
in the experiments (GPT-6 Luna and Sol, Claude Haiku 5.5 and Sonnet 5.5) are separate API calls made by the
code, not part of how this project was written. We are responsible for all claims here. See
`CONTRIBUTIONS.md` for who did what.

## Related work

- AgentDojo (Debenedetti et al., 2024): dynamic environment for prompt-injection attacks and
  defenses in tool-using agents.
- PromptArmor (Shi et al., 2025): prompts an off-the-shelf LLM to detect and remove injected
  prompts before the agent processes them.
- AgentSentry (Zhang et al., 2026): models multi-turn indirect injection as a temporal causal
  takeover and localizes it with counterfactual re-execution. TemporalGuard studies a different
  mechanism, a semantic judge over an adaptively widened window, and its cost.
- LogicInception (Liu et al., EMNLP 2026): an indirect prompt injection whose logic is split into
  declarative fragments spread over several tool outputs and tied together by fabricated causal
  dependencies, so that no fragment contains a command and the agent reconstructs the action by
  reasoning. The paper reports attack success of 42.9% to 48.8% on 1,139 scenarios against five
  defenses, with prompt-level defenses barely reducing it. It motivates the
  [LogicInception-style pilot](#logicinception-style-attacks-pilot) here: twelve author-written
  chains with benign twins, used to ask whether a judge that reads a window of outputs catches what a
  single read misses. Our numbers measure detection by a judge, not whether an agent carries out the
  attack, so they are not comparable with the paper's success rates.



## Gemini notes

### Gemini Batch API (LogicInception benign twins)

Install `pip install -e ".[gemini,dev]"` and set `GEMINI_API_KEY` in your shell.
The `gemini-batch` command supports `prepare`, `submit`, `status`, and `collect`.
The command uses Gemini's JSONL file-backed Batch API and fills the *same* cache
as `temporalguard eval --judge gemini`.

**Batchable strategies:** `per_message`, `fixed5`, and `full`. The adaptive
`fib_min3_fallback_confirm` strategy cannot be pre-batched because its next
window depends on the previous judge verdict. Run that strategy using `eval`.

PowerShell example (LI A; replace A with B for the second dataset):

```powershell
$common = @('--model','gemini-3.1-pro-preview',
  '--cache','runs/cache_gemini_pro.jsonl',
  '--workdir','runs/gemini_pro_li_a_twins_batch',
  '--li-file','data/li_attacks_A.csv',
  '--li-twin-file','data/li_benign_twins_A.csv',
  '--families','li','li_span','li_concat',
  '--per-family','12','--benign','0',
  '--strategies','per_message','full')
temporalguard gemini-batch prepare @common
temporalguard gemini-batch submit @common
temporalguard gemini-batch status @common
temporalguard gemini-batch collect @common
# If still running, use: temporalguard gemini-batch collect @common --wait
# Evaluate batch-cached windows; Fibonacci will make online calls.
temporalguard eval --judge gemini --model gemini-3.1-pro-preview `
  --cache runs/cache_gemini_pro.jsonl `
  --li-file data/li_attacks_A.csv --li-twin-file data/li_benign_twins_A.csv `
  --families li li_span li_concat --per-family 12 --benign 0 `
  --strategies per_message fib_min3_fallback_confirm full `
  --ci --by-family --out runs/liA_twin_gemini_pro.md
```

Do not delete the workdir until collection completes. If an existing batch has
already been submitted, use `status`/`collect`, not another `prepare`/`submit`.
This implementation was tested with mocked SDK responses, not a paid live job;
start with a small pilot to confirm compatibility with your installed SDK/model.

## Gemini adaptive batch evaluation

The `gemini-batch` subcommands support iterative cache-driven batching of adaptive Fibonacci windows. See `COMMANDS.md` Part 6.4 for the prepare/submit/collect loop and a no-direct-call final evaluation.

## License

MIT
