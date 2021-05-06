# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.combination_sum_ii import Solution
    return Solution()


@pytest.mark.parametrize(
    'candidates,target,expected',
    [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[2, 6], [1, 7], [1, 2, 5], [1, 1, 6]]),
        ([2, 5, 2, 1, 2], 5, [[5], [1, 2, 2]])
    ],
)
def test_combination_sum_ii(solution, candidates, target, expected):
    actual = solution.combinationSum2(candidates, target)
    assert all([a == b for a, b in zip(actual, expected)])
