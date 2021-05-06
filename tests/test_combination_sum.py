# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.combination_sum import Solution
    return Solution()


@pytest.mark.parametrize(
    'candidates,target,expected',
    [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
        ([1], 1, [[1]]),
        ([1], 2, [[1, 1]]),
    ],
)
def test_combination_sum(solution, candidates, target, expected):
    actual = solution.combinationSum(candidates, target)
    assert all([a == b for a, b in zip(actual, expected)])
