from types import SimpleNamespace

import pytest

from temporalguard.judge import JudgeError
from temporalguard.judge.anthropic_judge import AnthropicJudge
from temporalguard.models import ToolOutput

WINDOW = [ToolOutput(4, "web", "alpha"), ToolOutput(5, "web", "beta")]


class FakeMessages:
    def __init__(self, response=None, error=None):
        self.response, self.error, self.calls = response, error, []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return self.response


def fake_client(**kw):
    return SimpleNamespace(messages=FakeMessages(**kw))


def tool_use(payload):
    return SimpleNamespace(type="tool_use", input=payload)


def response(blocks, in_tok=120, out_tok=30):
    return SimpleNamespace(
        content=blocks, usage=SimpleNamespace(input_tokens=in_tok, output_tokens=out_tok)
    )


def test_forces_the_verdict_tool_and_parses_the_result():
    payload = {
        "malicious": True,
        "confidence": 0.9,
        "needs_more_context": False,
        "fragment_indices": [4, 5],
        "reconstructed_instruction": "combined",
        "attack_type": "data_exfiltration",
        "rationale": "because",
    }
    client = fake_client(response=response([SimpleNamespace(type="text"), tool_use(payload)]))
    judge = AnthropicJudge(model="test-model", client=client)
    result = judge.judge(WINDOW, task="do the thing")

    call = client.messages.calls[0]
    assert call["model"] == "test-model"
    assert call["tool_choice"] == {"type": "tool", "name": "record_verdict"}
    assert '<tool_output index="5"' in call["messages"][0]["content"]
    assert "do the thing" in call["messages"][0]["content"]

    assert result.malicious and result.fragment_indices == [4, 5]
    assert result.usage.input_tokens == 120 and result.usage.output_tokens == 30
    assert result.usage.calls == 1 and result.usage.latency_s >= 0


def test_api_failure_becomes_judge_error():
    judge = AnthropicJudge(client=fake_client(error=RuntimeError("rate limited")))
    with pytest.raises(JudgeError, match="rate limited"):
        judge.judge(WINDOW)


def test_missing_tool_block_becomes_judge_error():
    judge = AnthropicJudge(client=fake_client(response=response([SimpleNamespace(type="text")])))
    with pytest.raises(JudgeError, match="no tool_use"):
        judge.judge(WINDOW)


def test_malformed_verdict_becomes_judge_error():
    judge = AnthropicJudge(client=fake_client(response=response([tool_use({"malicious": True})])))
    with pytest.raises(JudgeError):
        judge.judge(WINDOW)
