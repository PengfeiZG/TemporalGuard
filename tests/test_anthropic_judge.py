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


# ---------------------------------------------------------- Sonnet 5.5 and tool_choice
def _payload():
    return {
        "malicious": True, "confidence": 0.9, "needs_more_context": False,
        "fragment_indices": [1], "reconstructed_instruction": "x", "rationale": "r",
    }  # fmt: skip


def test_sonnet_5_5_gets_auto_tool_choice_a_prompt_instruction_and_minimal_thinking(monkeypatch):
    monkeypatch.delenv("TEMPORALGUARD_ANTHROPIC_TOOL_CHOICE", raising=False)
    client = fake_client(response=response([tool_use(_payload())]))
    judge = AnthropicJudge(model="claude-sonnet-5-5", client=client)
    assert judge.tool_choice_mode == "auto"
    judge.judge(WINDOW)
    call = client.messages.calls[0]
    assert call["tool_choice"] == {"type": "auto"}
    assert call["thinking"] == {"type": "between_tools"}
    assert call["system"].endswith("Do not write any other text.")


def test_haiku_keeps_the_forced_tool_call_and_sends_no_thinking_setting(monkeypatch):
    monkeypatch.delenv("TEMPORALGUARD_ANTHROPIC_TOOL_CHOICE", raising=False)
    client = fake_client(response=response([tool_use(_payload())]))
    judge = AnthropicJudge(model="claude-haiku-5-5", client=client)
    assert judge.tool_choice_mode == "forced"
    judge.judge(WINDOW)
    call = client.messages.calls[0]
    assert call["tool_choice"] == {"type": "tool", "name": "record_verdict"}
    assert "thinking" not in call and not call["system"].endswith("any other text.")


def test_tool_choice_can_be_overridden_and_is_validated(monkeypatch):
    monkeypatch.delenv("TEMPORALGUARD_ANTHROPIC_TOOL_CHOICE", raising=False)
    assert (
        AnthropicJudge(
            model="claude-haiku-5-5", client=object(), tool_choice="auto"
        ).tool_choice_mode
        == "auto"
    )
    monkeypatch.setenv("TEMPORALGUARD_ANTHROPIC_TOOL_CHOICE", "forced")
    assert AnthropicJudge(model="claude-sonnet-5-5", client=object()).tool_choice_mode == "forced"
    with pytest.raises(ValueError):
        AnthropicJudge(client=object(), tool_choice="sometimes")


def test_models_known_to_reject_forced_tool_use():
    from temporalguard.judge.anthropic_judge import supports_forced_tool_use

    assert supports_forced_tool_use("claude-haiku-5-5")
    for m in ("claude-sonnet-5-5", "claude-opus-5-5", "claude-fable-5-1", "claude-mythos-5-1"):
        assert not supports_forced_tool_use(m), m


def test_cache_keys_are_unchanged_for_forced_judges_and_differ_for_auto(tmp_path):
    import hashlib
    import json

    from temporalguard.judge import CachingJudge
    from temporalguard.judge.prompts import SYSTEM_PROMPT, build_user_message

    forced = AnthropicJudge(model="claude-haiku-5-5", client=object())
    old_key = hashlib.sha256(
        json.dumps(
            ["anthropic", "claude-haiku-5-5", None, SYSTEM_PROMPT, build_user_message(WINDOW, "t")]
        ).encode("utf-8")
    ).hexdigest()
    assert CachingJudge(forced)._key(WINDOW, "t") == old_key  # existing caches keep working
    auto = AnthropicJudge(model="claude-haiku-5-5", client=object(), tool_choice="auto")
    assert CachingJudge(auto)._key(WINDOW, "t") != old_key


class SequencedMessages:
    """Returns the queued responses one per call, then repeats the last one."""

    def __init__(self, responses):
        self.responses, self.calls = list(responses), []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return self.responses.pop(0) if len(self.responses) > 1 else self.responses[0]


def _text_only():
    return response([SimpleNamespace(type="text", text="I think it is an attack.")], 100, 20)


def test_auto_mode_retries_when_the_model_answers_in_text_and_sums_the_usage():
    client = SimpleNamespace(
        messages=SequencedMessages([_text_only(), response([tool_use(_payload())], 120, 30)])
    )
    judge = AnthropicJudge(model="claude-sonnet-5-5", client=client)
    result = judge.judge(WINDOW)
    assert result.malicious and len(client.messages.calls) == 2
    second = client.messages.calls[1]["messages"]
    assert [m["role"] for m in second] == ["user", "assistant", "user"]
    assert second[1]["content"] == "I think it is an attack."
    assert "record_verdict" in second[2]["content"]
    assert (result.usage.input_tokens, result.usage.output_tokens, result.usage.calls) == (
        220,
        50,
        2,
    )


def test_auto_mode_gives_up_after_the_configured_retries_with_a_clear_error():
    client = SimpleNamespace(messages=SequencedMessages([_text_only()]))
    judge = AnthropicJudge(model="claude-sonnet-5-5", client=client, tool_retries=2)
    with pytest.raises(
        JudgeError, match=r"after 3 attempts, stop_reason=.*last text: 'I think it is an attack"
    ):
        judge.judge(WINDOW)
    assert len(client.messages.calls) == 3


def test_forced_mode_is_never_retried():
    client = SimpleNamespace(messages=SequencedMessages([_text_only()]))
    judge = AnthropicJudge(model="claude-haiku-5-5", client=client)
    with pytest.raises(JudgeError, match=r"after 1 attempt, stop_reason="):
        judge.judge(WINDOW)
    assert len(client.messages.calls) == 1


def test_auto_models_get_a_larger_token_budget_and_the_error_names_the_stop_reason(monkeypatch):
    monkeypatch.delenv("TEMPORALGUARD_ANTHROPIC_TOOL_CHOICE", raising=False)
    assert AnthropicJudge(model="claude-sonnet-5-5", client=object()).max_tokens == 2000
    assert AnthropicJudge(model="claude-haiku-5-5", client=object()).max_tokens == 600
    assert (
        AnthropicJudge(model="claude-sonnet-5-5", client=object(), max_tokens=900).max_tokens == 900
    )

    cut = response([], 100, 600)
    cut.stop_reason = "max_tokens"
    client = SimpleNamespace(messages=SequencedMessages([cut]))
    judge = AnthropicJudge(model="claude-sonnet-5-5", client=client)
    with pytest.raises(JudgeError, match=r"stop_reason=max_tokens\); last text: ''"):
        judge.judge(WINDOW)
    assert client.messages.calls[0]["max_tokens"] == 2000
