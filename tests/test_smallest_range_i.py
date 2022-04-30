# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.smallest_range_i import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, k, expected',
    [
        ([1], 0, 0),
        ([0, 10], 2, 6),
        ([1, 3, 6], 3, 0),
    ],
)
def test_smallest_range_i(solution, nums, k, expected):
    actual = solution.smallestRangeI(nums, k)
    assert expected == actual
