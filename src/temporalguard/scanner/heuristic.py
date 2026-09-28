"""Cheap lexical risk scanner.

The scanner looks only at the NEWEST tool output and returns a risk score in [0, 1]. It is the
cost gate: outputs below the gate threshold are allowed without calling the LLM judge. It is not
the security boundary; its job is to be cheap and to err toward flagging anything that reads like
a directive aimed at the agent. How many real fragments it lets through is itself a measured
quantity (the gate miss rate in the evaluation).
"""

from __future__ import annotations

import re
from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass

from ..models import ToolOutput


class Scanner(ABC):
    @abstractmethod
    def score(self, output: ToolOutput, history: Sequence[ToolOutput] = ()) -> float:
        """Risk score in [0, 1] for `output`. `history` holds earlier outputs, oldest first."""


@dataclass(frozen=True)
class Feature:
    name: str
    pattern: re.Pattern[str]
    weight: float


def _rx(pattern: str) -> re.Pattern[str]:
    return re.compile(pattern, re.IGNORECASE)


DEFAULT_FEATURES: tuple[Feature, ...] = (
    Feature(
        "override",
        _rx(
            r"\b(ignore|disregard|forget|override|supersed\w*|outdated|retired|"
            r"no longer appl\w*|take[s]? priority)\b"
        ),
        0.35,
    ),
    Feature(
        "instruction_ref",
        _rx(r"\b(instructions?|rules?|guidance|restrictions?|configuration|policy|prompt)\b"),
        0.15,
    ),
    Feature(
        "agent_address",
        _rx(r"\b(assistant|ai|agent|model|automated (reader|system)s?|you must|you should)\b"),
        0.15,
    ),
    Feature(
        "sensitive_data",
        _rx(
            r"\b(token|password|credential\w*|secret\w*|api[ _-]?key|access key|"
            r"environment variables?)\b"
        ),
        0.3,
    ),
    Feature(
        "outbound_verb",
        _rx(r"\b(send|e-?mail|post|forward|transmit|upload|share)\b"),
        0.15,
    ),
    Feature("destination", _rx(r"[\w.+-]+@[\w-]+\.[\w.]+|https?://\S+|\bendpoint\b"), 0.15),
    Feature(
        "continuation",
        _rx(
            r"\b(next stage|stage \d|step \d|next step|the following|to continue|"
            r"resulting value|procedure)\b"
        ),
        0.15,
    ),
    Feature("encoded_blob", _rx(r"\b[A-Za-z0-9+/]{40,}={0,2}"), 0.3),
)


class HeuristicScanner(Scanner):
    """Noisy-OR combination of weighted lexical features over the newest output.

    risk = 1 - prod(1 - weight_i) over the matched features. With the defaults one weak cue stays
    under the 0.2 gate, while a strong cue or two weak cues together pass it.
    """

    def __init__(self, features: Sequence[Feature] = DEFAULT_FEATURES) -> None:
        self.features = tuple(features)

    def matched(self, text: str) -> list[str]:
        return [f.name for f in self.features if f.pattern.search(text)]

    def score(self, output: ToolOutput, history: Sequence[ToolOutput] = ()) -> float:
        keep = 1.0
        for feature in self.features:
            if feature.pattern.search(output.content):
                keep *= 1.0 - feature.weight
        return round(1.0 - keep, 4)
