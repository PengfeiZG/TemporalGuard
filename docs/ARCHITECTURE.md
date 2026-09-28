# Architecture

## Goal

Detect a prompt injection whose intent only emerges across several tool outputs, without paying
for a full-history LLM scan on every output.

## Data flow

```
                    New tool output (index i)
                              │
                              ▼
                   ┌────────────────────┐
                   │  Scanner (no LLM)  │  risk in [0,1] from lexical features of output i
                   └─────────┬──────────┘
                             │
             risk < gate_threshold and gate enabled?
                  yes │                    │ no
                      ▼                    ▼
                    ALLOW        ┌────────────────────────┐
                (stage="gate")   │ Temporal context engine │
                                 │  sizes = schedule(n)    │  n = outputs so far
                                 └───────────┬─────────────┘
                                             │  for w in sizes (ascending):
                                             ▼
                                 ┌────────────────────────┐
                                 │ LLM judge on last w     │  structured verdict via forced tool call
                                 └───────────┬─────────────┘
                                             │
                          confident (>= stop_confidence) and not
                          "benign but needs more context"?
                             yes │                     │ no: next w (or end of schedule)
                                 ▼
                     verdict policy ─► ALLOW / QUARANTINE / BLOCK
```

Every decision records the windows examined, all judge results, token usage, the fragment indices
the judge named, and a rationale, so runs are auditable and cost is measurable.

## Modules

| module | responsibility |
|---|---|
| `models.py` | `ToolOutput`, `Verdict`, `JudgeResult`, `Decision`, `Usage` |
| `config.py` | `EngineConfig` thresholds and failure policies, validated |
| `schedules.py` | window schedules and coverage/blind-spot helpers |
| `scanner/heuristic.py` | noisy-OR lexical risk score (the cost gate) |
| `judge/base.py` | `Judge` interface, `JudgeError`, verdict validation |
| `judge/prompts.py` | system prompt, verdict tool schema, tag neutralization |
| `judge/anthropic_judge.py` | Claude Messages API judge with forced `record_verdict` tool use |
| `judge/mock.py` | offline stand-in that composes fragment categories (testing only) |
| `engine.py` | `TemporalGuard`: history, gate, escalation, verdict |
| `strategies.py` | named (schedule, gate) configurations used in experiments |
| `eval/` | fixtures, episode builder, metrics, runner, reports |
| `cli.py` | command line entry points |

## Escalation algorithm

```
inspect(output):
    history.append(output)
    risk = scanner.score(output)
    if gate and risk < gate_threshold: return ALLOW            # no LLM call
    for w in schedule.windows(len(history)):                   # ascending window sizes
        r = judge(history[-w:])                                # verdict on the NEWEST output
        confident = r.confidence >= stop_confidence
        wants_more = (not r.malicious) and r.needs_more_context
        if confident and not wants_more: break
    return policy(r)
```

Verdict policy: not malicious or confidence < `flag_min_confidence` → ALLOW; malicious with
confidence ≥ `block_confidence` → BLOCK; otherwise QUARANTINE. If the widest window is still
unconfident, `on_ambiguous` chooses between following the label, quarantining (fail closed), or
allowing (fail open). If the judge errors, `on_error` applies (default: quarantine).

## Design decisions

1. **The schedule never changes semantics.** It only picks which window sizes are tried and in
   what order. This keeps the Fibonacci question a clean cost/coverage comparison.
2. **The gate is a separate factor.** Strategies come in gated and ungated forms so savings from
   skipping the judge are not credited to the window schedule.
3. **`gated_full` is a first-class baseline.** Without "cheap gate, then one full-context judge",
   the schedule's benefit cannot be separated from the gate's.
4. **Structured, validated verdicts.** The Claude judge forces a `record_verdict` tool call and
   `parse_verdict` clamps confidence, drops unknown fragment indices, and rejects malformed
   output rather than guessing.
5. **The judge is treated as attackable.** Outputs are wrapped in `<tool_output>` tags, tag-like
   text inside content is neutralized, and the system prompt tells the judge to treat the content
   as data.
6. **Fail closed by default.** Judge failure quarantines the output. Deployments that prefer
   availability can set `on_error="allow"`.
7. **Quarantined outputs stay in history.** They are withheld from the agent but still visible to
   later windows, so a fragment that was withheld can still help identify the rest.

## Cost model

Worst case (no early stop) at history length `n` is `sum(windows(n))` outputs of context. For
n = 20: Fibonacci 32, power-of-two 31, linear-4 45, full 20. Escalation therefore only helps when
most decisions stop at small windows or the gate skips the judge entirely. Provider prompt caching
changes real dollar cost and is not modeled by `estimate_tokens`; the Claude judge reports actual
usage. `temporalguard schedules --n N` prints these figures for any history length.

## Threat model and known gaps

- **Blind spot.** A schedule whose largest window is smaller than the history never sees the
  oldest outputs. An attacker who knows the schedule could place a fragment there. Mitigations to
  evaluate: `WithFullFallback`, periodic full scans, provenance-based retention of risky outputs.
- **Gate misses.** A fragment that looks harmless lexically is never judged. The evaluation
  reports `gate_miss_rate`; the bundled fixtures use strong cues, so their rate is optimistic.
- **Judge error and manipulation.** The judge is an LLM reading untrusted text.
- **Out of scope for v0.1:** paraphrased/encoded/cross-tool fragments, multimodal content, memory
  poisoning, and enforcement beyond returning a verdict (the host application decides what to do).

## Evaluation plan

1. Build distributed episodes from AgentDojo attacks, placed with adjacent, spaced,
   Fibonacci-gap and long-context patterns among ordinary outputs, plus benign sessions with
   look-alike content (`eval/episodes.py`; the AgentDojo adapter is future work).
2. Run every strategy in `strategies.py` with the same judge and prompts.
3. Report the metrics in `eval/metrics.py`; compare `fib` against `pow2`, `fixed5`, `full` and
   `gated_full` on recall, false positives, and tokens.
4. Add a schedule-aware adaptive attacker and re-measure.
5. Report null results as results.
