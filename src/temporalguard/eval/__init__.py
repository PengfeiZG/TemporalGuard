"""Evaluation harness: synthetic fixtures, episode construction, metrics, stats, and the runner."""

from .episodes import (
    Episode,
    adaptive_suite,
    build_suite,
    episodes_from_json,
    episodes_to_json,
)
from .metrics import summarize, summarize_by_family
from .runner import compare, compare_adaptive, run_many, run_strategy
from .stats import bootstrap_ci, paired_difference

__all__ = [
    "Episode",
    "adaptive_suite",
    "bootstrap_ci",
    "build_suite",
    "compare",
    "compare_adaptive",
    "episodes_from_json",
    "episodes_to_json",
    "paired_difference",
    "run_many",
    "run_strategy",
    "summarize",
    "summarize_by_family",
]
