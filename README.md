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

> **Status: v0.1 scaffold.** The engine, judges, window schedules, metrics and an offline harness
> work and are tested. There are **no research results yet.** The bundled fixtures are tiny and
> synthetic, and the offline mock judge is a plumbing stand-in, not a security model. See
> [Status and limitations](#status-and-limitations).

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
pip install -e ".[dev]"            # core + tests
pip install -e ".[anthropic]"      # adds the Claude-backed judge
pip install -e ".[openai]"         # adds the OpenAI-backed judge
```

Python 3.10+. The core has no runtime dependencies.

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

## Repository layout

```
src/temporalguard/
  engine.py         TemporalGuard: gate, escalation loop, verdict policy
  schedules.py      Fibonacci, PowerOfTwo, Linear, Fixed, Full, WithFullFallback
  scanner/          cheap lexical risk scorer (the gate)
  judge/            Judge interface, Claude judge, offline mock judge, prompts
  strategies.py     the named configurations above
  eval/             fixtures, episode builder, metrics, runner, report
  cli.py            temporalguard schedules | demo | make-suite | eval
tests/              pytest suite (no network)
docs/ARCHITECTURE.md
examples/quickstart.py
```

## Status and limitations

- **Mock judge numbers are not results.** It exists so the pipeline and metrics can be tested
  without cost. Any table produced with `--judge mock` only demonstrates that the plumbing works.
- **Fixtures are synthetic and small** (four lexical and three paraphrased fragment sets, a few
  benign look-alikes). The planned benchmark derives distributed episodes from the AgentDojo task
  suites; that adapter is not written yet.
- **Not implemented yet:** the AgentDojo-derived benchmark, encoded and cross-tool fragment
  families, and results from a real judge. The schedule-aware attacker and the fallback mitigation
  exist and are tested with the mock judge only.
- **Mock-judge comparisons between schedules are artifacts**, not findings. The mock keys on the
  same keywords as the scanner and the fixtures, so schedule differences it shows depend on how the
  mock composes categories.
- **Cost is not automatically lower.** Escalating through 1,2,3,5,8,13 costs 32 outputs' worth of
  context in the worst case at n = 20, more than one full scan. Savings only appear if most
  decisions stop early, which is why `gated_full` is a required baseline.
- **This is a research prototype, not a complete defense.** The judge is itself an LLM reading
  untrusted text. Tool outputs are wrapped and boundary tags are neutralized, but the judge can
  still be wrong or manipulated. Combine with least-privilege tool permissions.

## Related work

- AgentDojo (Debenedetti et al., 2024): dynamic environment for prompt-injection attacks and
  defenses in tool-using agents.
- PromptArmor (Shi et al., 2025): prompts an off-the-shelf LLM to detect and remove injected
  prompts before the agent processes them.
- AgentSentry (Zhang et al., 2026): models multi-turn indirect injection as a temporal causal
  takeover and localizes it with counterfactual re-execution. TemporalGuard studies a different
  mechanism, a semantic judge over an adaptively widened window, and its cost.

Verify these citations against the papers before publishing anything.

## License

MIT
