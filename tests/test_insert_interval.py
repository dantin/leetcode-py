# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.insert_interval import Solution
    return Solution()


@pytest.mark.parametrize(
    'intervals, newInterval, expected',
    [
        ([[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]]),
        ([],
            [5, 7],
            [[5, 7]]),
        ([[1, 5]],
            [2, 3],
            [[1, 5]]),
        ([[1, 5]],
            [2, 7],
            [[1, 7]]),
    ],
)
def test_insert(solution, intervals, newInterval, expected):
    actual = solution.insert(intervals, newInterval)
    assert expected == actual
