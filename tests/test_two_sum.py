# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.two_sum import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([2, 7, 11, 15], 9, [1, 0]),
        ([3, 2, 4], 6, [2, 1]),
        ([3, 3], 6, [1, 0]),
    ],
)
def test_two_sum_v1(solution, nums, target, expected):
    actual = solution.twoSum(nums, target)
    assert len(expected) == len(actual)
    assert all([a == b for a, b in zip(actual, expected)])


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum_v2(solution, nums, target, expected):
    actual = solution.twoSum2(nums, target)
    assert len(expected) == len(actual)
    assert all([a == b for a, b in zip(actual, expected)])
