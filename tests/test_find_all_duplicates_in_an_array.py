# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.find_all_duplicates_in_an_array import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([4, 3, 2, 7, 8, 2, 3, 1], [3, 2]),
        ([1, 1, 2], [1]),
        ([1], []),
    ],
)
def test_find_duplicates(solution, nums, expected):
    actual = solution.findDupicates(nums)
    assert expected == actual
