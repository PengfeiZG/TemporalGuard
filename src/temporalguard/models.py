"""Core data types shared across TemporalGuard."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Verdict(str, Enum):
    """What the firewall does with the newest tool output."""

    ALLOW = "allow"  # pass the output to the agent unchanged
    QUARANTINE = "quarantine"  # withhold the output, keep the session going
    BLOCK = "block"  # withhold the output and halt the tool chain

    @property
    def flagged(self) -> bool:
        return self is not Verdict.ALLOW


@dataclass(frozen=True)
class ToolOutput:
    """One tool result observed by the agent. `index` is its position in the session."""

    index: int
    tool: str
    content: str


@dataclass
class Usage:
    """LLM usage for one judge call or, summed, for one decision."""

    input_tokens: int = 0
    output_tokens: int = 0
    calls: int = 0
    latency_s: float = 0.0

    def add(self, other: Usage) -> None:
        self.input_tokens += other.input_tokens
        self.output_tokens += other.output_tokens
        self.calls += other.calls
        self.latency_s += other.latency_s

    @property
    def total_tokens(self) -> int:
        return self.input_tokens + self.output_tokens


@dataclass
class JudgeResult:
    """Structured verdict from the semantic judge for one context window."""

    malicious: bool  # is the NEWEST output part of, or completing, an injected instruction?
    confidence: float  # confidence that `malicious` is the right label, in [0, 1]
    needs_more_context: bool = False  # newest output looks like an incomplete fragment
    fragment_indices: list[int] = field(default_factory=list)  # absolute session indices
    reconstructed_instruction: str = ""
    attack_type: str = "none"
    rationale: str = ""
    usage: Usage = field(default_factory=Usage)


@dataclass
class Decision:
    """The firewall's decision for one tool output, with everything needed to audit it."""

    verdict: Verdict
    output_index: int
    stage: str  # "gate" | "judge" | "judge_error"
    risk_score: float
    windows_examined: list[int] = field(default_factory=list)
    judge_results: list[JudgeResult] = field(default_factory=list)
    fragment_indices: list[int] = field(default_factory=list)
    reconstructed_instruction: str = ""
    explanation: str = ""
    usage: Usage = field(default_factory=Usage)

    @property
    def context_examined(self) -> int:
        """Outputs shown to the judge, summed over every call for this decision."""
        return sum(self.windows_examined)
