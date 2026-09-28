import pytest

from temporalguard.schedules import (
    Fibonacci,
    Fixed,
    Full,
    Linear,
    PowerOfTwo,
    WithFullFallback,
    blind_spot,
    coverage_stats,
)


def test_fibonacci_windows():
    assert Fibonacci().windows(20) == [1, 2, 3, 5, 8, 13]
    assert Fibonacci().windows(1) == [1]
    assert Fibonacci().windows(0) == []


def test_power_of_two_windows():
    assert PowerOfTwo().windows(20) == [1, 2, 4, 8, 16]
    assert PowerOfTwo().windows(16) == [1, 2, 4, 8, 16]


def test_linear_fixed_full():
    assert Linear(4).windows(20) == [1, 5, 9, 13, 17]
    assert Fixed(5).windows(3) == [3]
    assert Fixed(5).windows(20) == [5]
    assert Full().windows(7) == [7]
    assert Full().windows(0) == []


@pytest.mark.parametrize("bad", [0, -1])
def test_invalid_parameters(bad):
    with pytest.raises(ValueError):
        Fixed(bad)
    with pytest.raises(ValueError):
        Linear(bad)


def test_windows_are_ascending_and_within_history():
    for schedule in (Fibonacci(), PowerOfTwo(), Linear(3), Fixed(4), Full()):
        for n in range(1, 40):
            w = schedule.windows(n)
            assert w == sorted(set(w))
            assert all(1 <= x <= n for x in w)


def test_fallback_appends_full_window_once():
    s = WithFullFallback(Fibonacci())
    assert s.windows(20) == [1, 2, 3, 5, 8, 13, 20]
    assert s.windows(13) == [1, 2, 3, 5, 8, 13]


def test_blind_spot_and_worst_case_cost():
    assert blind_spot(Fibonacci(), 20) == 7
    assert blind_spot(Full(), 20) == 0
    stats = coverage_stats(Fibonacci(), 20)
    assert stats["worst_case_context"] == 32  # 1+2+3+5+8+13, more than one full scan of 20
    assert stats["worst_case_vs_full"] == 1.6
