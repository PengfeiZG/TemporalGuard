"""Evaluation harness: synthetic fixtures, episode construction, metrics, and the runner."""

from .episodes import Episode, build_suite, episodes_from_json, episodes_to_json
from .metrics import summarize
from .runner import compare, run_strategy

__all__ = [
    "Episode",
    "build_suite",
    "compare",
    "episodes_from_json",
    "episodes_to_json",
    "run_strategy",
    "summarize",
]
