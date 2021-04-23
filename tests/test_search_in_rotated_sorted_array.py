# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.search_in_rotated_sorted_array import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
    ],
)
def test_search_in_rotated_sorted_array(solution, nums, target, expected):
    actual = solution.search(nums, target)
    assert actual == expected
