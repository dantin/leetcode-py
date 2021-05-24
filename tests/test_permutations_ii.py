# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.permutations_ii import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ],
)
def test_permutations_ii(solution, nums, expected):
    actual = solution.permuteUnique(nums)
    assert actual == expected
