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
temporalguard eval --judge anthropic --model claude-haiku-4-5-20251001 \
    --price-in <USD/Mtok> --price-out <USD/Mtok> --format csv --out results.csv
```

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

Running the schedule comparison with and without the gate separates two effects that are easy to
conflate: savings from *skipping* the judge on low-risk outputs, and savings from *how the window
grows*.

## Metrics

Attack success rate (1 − recall), early containment (flagged before the final fragment arrives),
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
- **Fixtures are synthetic and tiny** (four fragment sets, a few benign look-alikes). The planned
  benchmark derives distributed episodes from the AgentDojo task suites; that adapter is not
  written yet.
- **Not implemented yet:** the AgentDojo-derived benchmark, paraphrased/encoded/cross-tool
  fragment families, and an adaptive attacker that knows the window schedule. Until then the
  schedule's blind spot (see `temporalguard schedules`) is a known, unmeasured weakness: any
  schedule that never inspects the whole history can miss fragments older than its largest
  window. `WithFullFallback` exists as a mitigation to evaluate.
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
