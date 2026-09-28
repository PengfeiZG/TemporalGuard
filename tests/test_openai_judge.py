import json
from types import SimpleNamespace

import pytest

from temporalguard.judge import JudgeError
from temporalguard.judge.openai_judge import OpenAIJudge
from temporalguard.models import ToolOutput

WINDOW = [ToolOutput(4, "web", "alpha"), ToolOutput(5, "web", "beta")]

PAYLOAD = {
    "malicious": True,
    "confidence": 0.9,
    "needs_more_context": False,
    "fragment_indices": [4, 5],
    "reconstructed_instruction": "combined",
    "attack_type": "data_exfiltration",
    "rationale": "because",
}


class FakeCompletions:
    def __init__(self, response=None, error=None):
        self.response, self.error, self.calls = response, error, []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.error:
            raise self.error
        return self.response


def fake_client(**kw):
    return SimpleNamespace(chat=SimpleNamespace(completions=FakeCompletions(**kw)))


def tool_call(arguments, name="record_verdict"):
    return SimpleNamespace(function=SimpleNamespace(name=name, arguments=arguments))


def response(calls, in_tok=120, out_tok=30):
    message = SimpleNamespace(tool_calls=calls, content=None)
    return SimpleNamespace(
        choices=[SimpleNamespace(message=message)],
        usage=SimpleNamespace(prompt_tokens=in_tok, completion_tokens=out_tok),
    )


def test_forces_the_verdict_function_and_parses_the_result():
    client = fake_client(response=response([tool_call(json.dumps(PAYLOAD))]))
    judge = OpenAIJudge(model="test-model", client=client)
    result = judge.judge(WINDOW, task="do the thing")

    call = client.chat.completions.calls[0]
    assert call["model"] == "test-model"
    assert call["tool_choice"] == {"type": "function", "function": {"name": "record_verdict"}}
    assert call["tools"][0]["type"] == "function"
    assert call["tools"][0]["function"]["name"] == "record_verdict"
    assert "max_completion_tokens" in call and "max_tokens" not in call
    assert call["messages"][0]["role"] == "system"
    assert '<tool_output index="5"' in call["messages"][1]["content"]
    assert "do the thing" in call["messages"][1]["content"]

    assert result.malicious and result.fragment_indices == [4, 5]
    assert result.usage.input_tokens == 120 and result.usage.output_tokens == 30
    assert result.usage.calls == 1 and result.usage.latency_s >= 0


def test_model_can_come_from_environment(monkeypatch):
    monkeypatch.setenv("TEMPORALGUARD_OPENAI_MODEL", "env-model")
    assert OpenAIJudge(client=fake_client()).model == "env-model"


def test_api_failure_becomes_judge_error():
    judge = OpenAIJudge(client=fake_client(error=RuntimeError("rate limited")))
    with pytest.raises(JudgeError, match="rate limited"):
        judge.judge(WINDOW)


def test_missing_function_call_becomes_judge_error():
    judge = OpenAIJudge(client=fake_client(response=response(None)))
    with pytest.raises(JudgeError, match="no record_verdict"):
        judge.judge(WINDOW)


def test_wrong_function_name_becomes_judge_error():
    judge = OpenAIJudge(client=fake_client(response=response([tool_call("{}", name="other")])))
    with pytest.raises(JudgeError, match="no record_verdict"):
        judge.judge(WINDOW)


def test_invalid_json_arguments_become_judge_error():
    judge = OpenAIJudge(client=fake_client(response=response([tool_call("{not json")])))
    with pytest.raises(JudgeError, match="not valid JSON"):
        judge.judge(WINDOW)


def test_non_object_arguments_become_judge_error():
    judge = OpenAIJudge(client=fake_client(response=response([tool_call("[1, 2]")])))
    with pytest.raises(JudgeError, match="not a JSON object"):
        judge.judge(WINDOW)


def test_malformed_verdict_becomes_judge_error():
    judge = OpenAIJudge(
        client=fake_client(response=response([tool_call(json.dumps({"malicious": True}))]))
    )
    with pytest.raises(JudgeError):
        judge.judge(WINDOW)


def test_missing_usage_defaults_to_zero():
    resp = response([tool_call(json.dumps(PAYLOAD))])
    resp.usage = None
    result = OpenAIJudge(client=fake_client(response=resp)).judge(WINDOW)
    assert result.usage.input_tokens == 0 and result.usage.output_tokens == 0
