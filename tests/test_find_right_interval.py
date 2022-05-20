# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.find_right_interval import Solution
    return Solution()


@pytest.mark.parametrize(
    'intervals, expected',
    [
        ([[1, 2]], [-1]),
        ([[3, 4], [2, 3], [1, 2]], [-1, 0, 1]),
        ([[1, 4], [2, 3], [3, 4]], [-1, 2, -1]),
    ],
)
def test_find_right_interval(solution, intervals, expected):
    actual = solution.findRightInterval(intervals)
    assert expected == actual
