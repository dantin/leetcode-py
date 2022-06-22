# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.maximum_subarray import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ],
)
def test_max_subarray(solution, nums, expected):
    actual = solution.maxSubArray(nums)
    assert expected == actual
