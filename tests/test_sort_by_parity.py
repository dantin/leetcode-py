# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.sort_array_by_parity import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, ,expected',
    [
        ([3, 1, 2, 4], [4, 2, 1, 3]),
        ([0], [0]),
    ],
)
def test_sort_by_parity(solution, nums, expected):
    actual = solution.sortArrayByParity(nums)
    assert actual == expected
