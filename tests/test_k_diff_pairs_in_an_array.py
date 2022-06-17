# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.k_diff_pairs_in_an_array import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, k, expected',
    [
        ([3, 1, 4, 1, 5], 2, 2),
        ([1, 2, 3, 4, 5], 1, 4),
        ([1, 3, 1, 5, 4], 0, 1),
    ],
)
def test_find_pairs(solution, nums, k, expected):
    actual = solution.findPairs(nums, k)
    assert expected == actual
