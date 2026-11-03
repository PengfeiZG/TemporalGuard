"""Offline Gemini adapter tests; no real API calls."""

import json
import sys
from types import SimpleNamespace

import pytest

from temporalguard.judge.base import JudgeError
from temporalguard.judge.gemini_judge import GeminiJudge
from temporalguard.models import ToolOutput


class FakeModels:
    def __init__(self, text):
        self.text = text

    def generate_content(self, **kwargs):
        return SimpleNamespace(
            text=self.text,
            usage_metadata=SimpleNamespace(
                prompt_token_count=12, candidates_token_count=8, thoughts_token_count=3
            ),
        )


@pytest.fixture(autouse=True)
def fake_google_sdk(monkeypatch):
    types = SimpleNamespace(GenerateContentConfig=lambda **kwargs: kwargs)
    monkeypatch.setitem(sys.modules, "google", SimpleNamespace(genai=SimpleNamespace(types=types)))
    monkeypatch.setitem(sys.modules, "google.genai", SimpleNamespace(types=types))


def test_gemini_valid_verdict():
    payload = dict(
        malicious=True,
        confidence=0.9,
        needs_more_context=False,
        fragment_indices=[0],
        reconstructed_instruction="redirect agent",
        attack_type="goal_hijack",
        rationale="instruction",
    )
    client = SimpleNamespace(models=FakeModels(json.dumps(payload)))
    judge = GeminiJudge(model="test-model", client=client)
    result = judge.judge([ToolOutput(0, "web", "malicious text")], "Summarize")
    assert result.malicious is True
    assert result.fragment_indices == [0]
    assert result.usage.input_tokens == 12
    assert result.usage.output_tokens == 11


def test_gemini_invalid_json_fails_closed():
    judge = GeminiJudge(client=SimpleNamespace(models=FakeModels("not json")))
    with pytest.raises(JudgeError):
        judge.judge([ToolOutput(0, "web", "text")])
