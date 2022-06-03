# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.first_missing_positive import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([2, 1], 3)
    ],
)
def test_first_missing_positive(solution, nums, expected):
    actual = solution.firstMissingPositive(nums)
    assert actual == expected
