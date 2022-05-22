# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.can_i_win import Solution
    return Solution()


@pytest.mark.parametrize(
    'max_choosible_integer, desired_total, expected',
    [
        (10, 11, False),
        (10, 0, True),
        (10, 1, True),
    ],
)
def test_can_i_win(solution, max_choosible_integer, desired_total, expected):
    actual = solution.canIWin(max_choosible_integer, desired_total)
    assert expected == actual
