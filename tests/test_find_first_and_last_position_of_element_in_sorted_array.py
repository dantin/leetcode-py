# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.find_first_and_last_position_of_element_in_sorted_array import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
    ],
)
def test_find_first_and_last_position_of_element_in_sorted_array(solution, nums, target, expected):
    actual = solution.searchRange(nums, target)
    assert actual == expected
