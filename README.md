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
and Sonnet 5.5) and is backed by the tables and judge-reasoning dumps in [`runs/`](runs/). The whole
experimental programme cost about $22 in API credit. See [Results](#results) for the findings and
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
python -m pip install -e ".[dev,anthropic,openai,semantic]"
python -m pytest -q                    # 188 tests, no network, no API key
```

Extras: `dev` (tests and linters), `anthropic` and `openai` (the judges), `semantic` (sentence-transformers
for the semantic gate; it pulls in PyTorch, which is large). The core has no runtime dependencies, so
`pip install -e ".[dev]"` is enough to run the offline harness with the mock judge.

Python: `requires-python >= 3.10`. The results in `runs/` were produced with **Python 3.13.14 on Windows 11**. The exact package versions are in
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
[`runs/COMMANDS.md`](runs/COMMANDS.md)). "Cheap" judges are GPT-6 Luna and Claude Haiku 5.5; "strong" judges
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

## Reproducing the results

- **Tables and reasoning.** `runs/*.md` are the result tables, `runs/*_dump.jsonl` hold the judges' stated
  reasoning for each decision, and `runs/COMMANDS.md` lists the exact command behind each file.
- **The verdict caches are not in the repository.** They are about 20 MB, and rebuilding them from scratch
  costs about $22 in API credit. Every judged run caches each (model, prompt, window) verdict, so rerunning a
  command with the same cache costs nothing. The offline mock judge reproduces the plumbing for free:
  `temporalguard eval --families adjacent paraphrased --per-family 2 --benign 2`.
- **Keys and models.** Set `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` in your shell; they are never written to
  files. OpenAI runs need `TEMPORALGUARD_OPENAI_REASONING_EFFORT=none`. The models are `gpt-6-luna`,
  `gpt-6-sol`, `claude-haiku-5-5` and `claude-sonnet-5-5`.
- **A cheap check that the code works:** `python -m pytest -q` runs 188 tests with no network.

## Repository layout

```
src/temporalguard/
  engine.py         gate, escalation loop, confirm-on-flag and fallback, verdict policy
  schedules.py      Fibonacci, PowerOfTwo, Linear, Fixed, Full, WithFullFallback
  scanner/          keyword gate, stateful gate, semantic gate (sentence embeddings)
  judge/            Claude and OpenAI judges, cascade judge, caching judge, offline mock judge
  strategies.py     the named configurations
  eval/             fixtures, AgentDojo-derived data, episode builder, metrics, runner, gate calibration, report
  cli.py            temporalguard schedules | demo | make-suite | eval | gate-calibrate
tests/              188 tests (no network)
docs/               ARCHITECTURE.md, AGENTDOJO_REVIEW.md (review sheet for the 27 derived attacks)
runs/               result tables, judge-reasoning dumps, COMMANDS.md, requirements_freeze.txt
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
- **Two vendors, one sample per window.** Each judge verdict is sampled once and cached.
- **Utility is measured only as false alarms.** We report false-alarm rates on benign sessions (synthetic and
  AgentDojo's own text). We did not run agent tasks end to end, so task completion is not measured.
- **The gate's exemplars overlap the benchmark.** The topic exemplars were written after reading AgentDojo's
  attack goals; the generic-exemplar results are the ones to report.
- **A cascade cannot raise detection above the cheap judge's.** It only sees windows the cheap judge flags.
- **The adaptive attacker targets the window schedules, not the cascade or the gate.** An attacker who knows
  the gate's exemplars or the strong judge was not tested.
- **Not tested:** larger models (for example Claude Opus), encoded and cross-tool fragment families, and
  GPT-6.1 Sol (it cannot do forced tool calls with reasoning disabled, which this judge needs).
- **The mock judge produces no results.** It exists so the pipeline and metrics can be tested without cost.
- **This is a research prototype, not a complete defense.** The judge is itself an LLM reading untrusted text.
  Tool outputs are wrapped and boundary tags are neutralized, but the judge can still be wrong or manipulated.
  Combine it with least-privilege tool permissions.

## AI assistance

We used Claude (Anthropic) throughout this project. Claude wrote and tested most of the code (the engine, the judges, the evaluation harness, the cascade and the gates), drafted the benchmark fragments and analysed the result tables. The research question, the design decisions and the scope were ours. We ran every experiment ourselves with our own API keys, reviewed the AgentDojo-derived fragments row by row and decided what to report. The models that act as judges in the experiments are separate API calls made by the code, not part of how this project was written. We are responsible for all claims here.

## Related work

- AgentDojo (Debenedetti et al., 2024): dynamic environment for prompt-injection attacks and
  defenses in tool-using agents.
- PromptArmor (Shi et al., 2025): prompts an off-the-shelf LLM to detect and remove injected
  prompts before the agent processes them.
- AgentSentry (Zhang et al., 2026): models multi-turn indirect injection as a temporal causal
  takeover and localizes it with counterfactual re-execution. TemporalGuard studies a different
  mechanism, a semantic judge over an adaptively widened window, and its cost.


## License

MIT
