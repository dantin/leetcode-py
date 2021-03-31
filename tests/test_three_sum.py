# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.three_sum import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([], []),
        ([0], []),
    ],
)
def test_three_sum(solution, nums, expected):
    actual = solution.threeSum(nums)
    assert actual == expected
