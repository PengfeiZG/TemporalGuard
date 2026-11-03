from temporalguard.config import EngineConfig
from temporalguard.eval import gemini_li_batch


def test_full_prefetch_generates_every_prefix_and_deduplicates():
    class Recorder:
        def __init__(self):
            self.windows = []

        def judge(self, window, task):
            self.windows.append(tuple(o.index for o in window))
            raise gemini_li_batch.NeedsBatch()

    from types import SimpleNamespace

    judge = Recorder()
    episodes = [
        SimpleNamespace(outputs=[("tool1", "a"), ("tool2", "b"), ("tool3", "c")], task="task")
    ]
    gemini_li_batch.prefetch_full(judge, episodes, EngineConfig())
    assert judge.windows == [(0,), (0, 1), (0, 1, 2)]


def test_fib_first_prefetch_for_li_episodes():
    from types import SimpleNamespace

    class Recorder:
        def __init__(self):
            self.windows = []

        def judge(self, window, task):
            self.windows.append(tuple(o.index for o in window))
            raise gemini_li_batch.NeedsBatch()

    judge = Recorder()
    episodes = [
        SimpleNamespace(
            outputs=[("tool1", "a"), ("tool2", "b"), ("tool3", "c"), ("tool4", "d")], task="task"
        )
    ]
    gemini_li_batch.prefetch_fib_first(judge, episodes, EngineConfig())
    assert len(judge.windows) == 4
    assert judge.windows[-1] == (1, 2, 3)
