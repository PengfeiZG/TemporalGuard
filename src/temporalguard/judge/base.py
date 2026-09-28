"""Judge interface and verdict parsing."""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from typing import Any

from ..models import JudgeResult, ToolOutput
from .prompts import ATTACK_TYPES


class JudgeError(RuntimeError):
    """The judge could not produce a verdict (API failure, malformed output, ...)."""


class Judge(ABC):
    name: str = "judge"

    @abstractmethod
    def judge(self, window: Sequence[ToolOutput], task: str | None = None) -> JudgeResult:
        """Judge the NEWEST output of `window` (oldest first) in the light of the whole window."""


def _as_bool(value: Any, field: str) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value.lower() in {"true", "false"}:
        return value.lower() == "true"
    raise JudgeError(f"field {field!r} is not a boolean: {value!r}")


def parse_verdict(raw: Mapping[str, Any], window: Sequence[ToolOutput]) -> JudgeResult:
    """Validate a raw verdict dict (for example a tool_use input) into a JudgeResult."""
    if not isinstance(raw, Mapping):
        raise JudgeError(f"verdict is not an object: {raw!r}")
    for field in ("malicious", "confidence"):
        if field not in raw:
            raise JudgeError(f"verdict missing required field {field!r}")
    try:
        confidence = float(raw["confidence"])
    except (TypeError, ValueError) as exc:
        raise JudgeError(f"confidence is not a number: {raw['confidence']!r}") from exc
    confidence = min(1.0, max(0.0, confidence))

    valid = {o.index for o in window}
    fragments: list[int] = []
    for item in raw.get("fragment_indices") or []:
        try:
            idx = int(item)
        except (TypeError, ValueError):
            continue
        if idx in valid and idx not in fragments:
            fragments.append(idx)

    attack_type = str(raw.get("attack_type") or "none")
    if attack_type not in ATTACK_TYPES:
        attack_type = "other"

    malicious = _as_bool(raw["malicious"], "malicious")
    return JudgeResult(
        malicious=malicious,
        confidence=confidence,
        needs_more_context=_as_bool(raw.get("needs_more_context", False), "needs_more_context"),
        fragment_indices=sorted(fragments) if malicious else [],
        reconstructed_instruction=str(raw.get("reconstructed_instruction") or ""),
        attack_type=attack_type if malicious else "none",
        rationale=str(raw.get("rationale") or ""),
    )
