"""Token estimation and optional dollar-cost accounting."""

from __future__ import annotations

import math
from dataclasses import dataclass

from .models import Usage


def estimate_tokens(text: str) -> int:
    """Rough token estimate (~4 characters per token). Real judges report exact usage."""
    return max(1, math.ceil(len(text) / 4))


@dataclass(frozen=True)
class PriceTable:
    """USD per million tokens. Prices change, so there are deliberately no built-in defaults."""

    input_per_mtok: float = 0.0
    output_per_mtok: float = 0.0

    def cost(self, usage: Usage) -> float:
        return (
            usage.input_tokens * self.input_per_mtok + usage.output_tokens * self.output_per_mtok
        ) / 1_000_000
