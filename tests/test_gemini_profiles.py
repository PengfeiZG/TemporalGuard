from argparse import Namespace

from temporalguard.cli import GEMINI_BATCH_PROFILES, build_parser, cmd_gemini_batch


def test_twin_profiles_and_default_model():
    parser = build_parser()
    for name in ('li-a-twin', 'li-b-twin'):
        args = parser.parse_args(['gemini-batch', 'prepare', '--profile', name,
                                  '--cache', 'runs/cache.jsonl', '--workdir', 'runs/job'])
        assert args.profile == name
        assert args.model == 'gemini-3.1-pro-preview'
        assert GEMINI_BATCH_PROFILES[name][1].endswith('.csv')
        assert not args.json


def test_flash_override_and_json_switch():
    args = build_parser().parse_args(['gemini-batch', 'prepare', '--profile', 'li-a-twin',
        '--model', 'gemini-3.1-flash-lite', '--json', '--cache', 'cache.jsonl', '--workdir', 'job'])
    assert args.model == 'gemini-3.1-flash-lite'
    assert args.json


def test_li_profiles_default_to_per_message_full_and_fib(monkeypatch):
    """Status profile selection should not require live API credentials."""
    from types import SimpleNamespace

    from temporalguard import cli
    from temporalguard.judge.cache import CachingJudge

    captured = []
    fake_judge = CachingJudge(SimpleNamespace(name="gemini", model="gemini-3.1-pro-preview"))
    monkeypatch.setattr(cli, "_make_judge", lambda *args: fake_judge)
    monkeypatch.setattr(cli.gemini_batch, "status", lambda judge, workdir: ("MOCK", None))
    for profile in ("li-a", "li-b"):
        args = Namespace(profile=profile, action="status", model=None, cache=None,
                         workdir=None, per_family=None, strategies=None, seed=0,
                         li_file=None, li_twin_file=None, json=False)
        assert cmd_gemini_batch(args) == 0
        assert args.strategies == ["per_message", "fib_min3_fallback_confirm", "full"]
        captured.append(args)
    assert len(captured) == 2


