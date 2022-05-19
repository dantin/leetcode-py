# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.minimum_moves_to_equal_array_elements_ii import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 2, 3], 2),
        ([1, 10, 2, 9], 16),
    ],
)
def test_min_moves2(solution, nums, expected):
    actual = solution.minMoves2(nums)
    assert expected == actual
