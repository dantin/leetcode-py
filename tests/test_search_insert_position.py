# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.search_insert_position import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,target,expected',
    [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
    ],
)
def test_search_insert_position(solution, nums, target, expected):
    actual = solution.searchInsert(nums, target)
    assert actual == expected
