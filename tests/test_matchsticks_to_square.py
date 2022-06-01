# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.matchsticks_to_square import Solution
    return Solution()


@pytest.mark.parametrize(
    'matchsticks, expected',
    [
        ([1, 1, 2, 2, 2], True),
        ([3, 3, 3, 3, 4], False),
    ],
)
def test_make_square(solution, matchsticks, expected):
    actual = solution.makesquare(matchsticks)
    assert expected == actual
