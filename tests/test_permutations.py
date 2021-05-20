# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.permutations import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
def test_permutations(solution, nums, expected):
    actual = solution.permute(nums)
    assert actual == expected
