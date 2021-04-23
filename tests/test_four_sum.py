# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.four_sum import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([], 0, []),
    ],
)
def test_four_sum(solution, nums, target, expected):
    actual = solution.fourSum(nums, target)
    assert actual == expected
