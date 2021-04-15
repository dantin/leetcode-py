# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.remove_duplicates_from_sorted_array import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ],
)
def test_remove_duplicates_from_sorted_array(solution, nums, expected):
    actual = solution.removeDuplicates(nums)
    assert actual == len(expected)
    assert expected == nums[:actual]
