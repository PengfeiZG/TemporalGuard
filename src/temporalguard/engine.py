"""The temporal context engine: gate, adaptive window escalation, semantic judge, verdict."""

from __future__ import annotations

from collections.abc import Sequence

from .config import EngineConfig
from .judge.base import Judge, JudgeError
from .models import Decision, JudgeResult, ToolOutput, Usage, Verdict
from .scanner.heuristic import Scanner
from .schedules import Fibonacci, WindowSchedule


class TemporalGuard:
    """Sits between tool outputs and the agent.

    For every new tool output it (1) scores the output with a cheap scanner and allows clearly
    low-risk output without any LLM call, (2) otherwise asks the LLM judge about progressively
    larger windows of recent outputs, following `schedule`, until the verdict is confident, and
    (3) maps the final judge verdict to ALLOW / QUARANTINE / BLOCK.

    The schedule controls only how much context is inspected and in what order. It never changes
    what counts as malicious.
    """

    def __init__(
        self,
        judge: Judge,
        scanner: Scanner | None = None,
        schedule: WindowSchedule | None = None,
        config: EngineConfig | None = None,
        gate: bool = True,
        task: str | None = None,
    ) -> None:
        if gate and scanner is None:
            raise ValueError("gate=True requires a scanner")
        self.judge = judge
        self.scanner = scanner
        self.schedule = schedule or Fibonacci()
        self.config = config or EngineConfig()
        self.gate = gate
        self.task = task
        self.history: list[ToolOutput] = []

    def reset(self) -> None:
        self.history = []

    # ------------------------------------------------------------------ public API
    def inspect(self, content: str, tool: str = "tool") -> Decision:
        """Register the next tool output and decide what to do with it."""
        output = ToolOutput(index=len(self.history), tool=tool, content=content)
        self.history.append(output)

        risk = self.scanner.score(output, self.history[:-1]) if self.scanner else 1.0
        if self.gate and risk < self.config.gate_threshold:
            return Decision(
                verdict=Verdict.ALLOW,
                output_index=output.index,
                stage="gate",
                risk_score=risk,
                explanation="below gate threshold, no LLM call",
            )
        return self._escalate(output, risk)

    def inspect_all(self, outputs: Sequence[tuple[str, str]]) -> list[Decision]:
        """Convenience: run (tool, content) pairs through `inspect` in order."""
        return [self.inspect(content, tool) for tool, content in outputs]

    # ------------------------------------------------------------------ internals
    def _window(self, size: int) -> list[ToolOutput]:
        limit = self.config.max_chars_per_output
        return [ToolOutput(o.index, o.tool, o.content[:limit]) for o in self.history[-size:]]

    def _escalate(self, output: ToolOutput, risk: float) -> Decision:
        cfg = self.config
        n = len(self.history)
        sizes = self.schedule.windows(n) or [n]
        if cfg.min_window > 1:
            sizes = [w for w in sizes if w >= cfg.min_window] or [sizes[-1]]
        decision = Decision(
            verdict=Verdict.ALLOW, output_index=output.index, stage="judge", risk_score=risk
        )
        usage = Usage()
        last: JudgeResult | None = None
        confident = False

        for i, size in enumerate(sizes):
            try:
                result = self.judge.judge(self._window(size), self.task)
            except JudgeError as exc:
                decision.stage = "judge_error"
                decision.explanation = f"judge failed: {exc}"
                decision.verdict = (
                    Verdict.QUARANTINE if cfg.on_error == "quarantine" else Verdict.ALLOW
                )
                decision.usage = usage
                return decision
            usage.add(result.usage)
            decision.windows_examined.append(size)
            decision.judge_results.append(result)
            last = result

            wants_more = (
                cfg.escalate_on_needs_context and not result.malicious and result.needs_more_context
            )
            if result.confidence >= cfg.stop_confidence and not wants_more:
                confident = True
                break
            if i == len(sizes) - 1:
                break

        assert last is not None
        decision.usage = usage
        decision.fragment_indices = list(last.fragment_indices)
        decision.reconstructed_instruction = last.reconstructed_instruction
        decision.explanation = last.rationale
        decision.verdict = self._verdict(last, confident)
        return decision

    def _verdict(self, result: JudgeResult, confident: bool) -> Verdict:
        cfg = self.config
        if not confident and cfg.on_ambiguous != "label":
            return Verdict.QUARANTINE if cfg.on_ambiguous == "quarantine" else Verdict.ALLOW
        if not result.malicious or result.confidence < cfg.flag_min_confidence:
            return Verdict.ALLOW
        return Verdict.BLOCK if result.confidence >= cfg.block_confidence else Verdict.QUARANTINE
