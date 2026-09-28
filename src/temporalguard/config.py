"""Engine configuration with validation."""

from __future__ import annotations

from dataclasses import dataclass

_AMBIGUOUS = {"label", "quarantine", "allow"}
_ERRORS = {"quarantine", "allow"}


@dataclass
class EngineConfig:
    """Thresholds and policies for the temporal context engine.

    gate_threshold: scanner risk below this is allowed without any LLM call (gated strategies).
    stop_confidence: escalation stops once the judge is at least this confident.
    block_confidence: a malicious verdict at or above this confidence is BLOCK, not QUARANTINE.
    flag_min_confidence: a malicious label below this confidence is treated as not flagged.
    escalate_on_needs_context: keep widening the window when a confident benign verdict still
        says the newest output needs older context to be interpreted.
    on_ambiguous: what to do if the widest window is still ambiguous: "label" follows the
        judge's label, "quarantine" fails closed, "allow" fails open.
    on_error: what to do when the judge fails: "quarantine" (default, fail closed) or "allow".
    max_chars_per_output: per-output truncation before text is sent to the judge.
    """

    gate_threshold: float = 0.2
    stop_confidence: float = 0.8
    block_confidence: float = 0.95
    flag_min_confidence: float = 0.5
    escalate_on_needs_context: bool = True
    on_ambiguous: str = "label"
    on_error: str = "quarantine"
    max_chars_per_output: int = 4000

    def __post_init__(self) -> None:
        for name in (
            "gate_threshold",
            "stop_confidence",
            "block_confidence",
            "flag_min_confidence",
        ):
            value = getattr(self, name)
            if not 0.0 <= value <= 1.0:
                raise ValueError(f"{name} must be in [0, 1], got {value}")
        if self.on_ambiguous not in _AMBIGUOUS:
            raise ValueError(f"on_ambiguous must be one of {sorted(_AMBIGUOUS)}")
        if self.on_error not in _ERRORS:
            raise ValueError(f"on_error must be one of {sorted(_ERRORS)}")
        if self.max_chars_per_output < 100:
            raise ValueError("max_chars_per_output must be at least 100")
