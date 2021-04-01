# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.three_sum_closest import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([-1, 2, 1, -4], 1, 2),
    ],
)
def test_three_sum_closest(solution, nums, target, expected):
    actual = solution.threeSumClosest(nums, target)
    assert actual == expected
