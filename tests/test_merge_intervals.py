# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.merge_intervals import Solution
    return Solution()


@pytest.mark.parametrize(
    'intervals, expected',
    [
        ([[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]],
            [[1, 5]])
    ],
)
def test_merge(solution, intervals, expected):
    actual = solution.merge(intervals)
    assert expected == actual
