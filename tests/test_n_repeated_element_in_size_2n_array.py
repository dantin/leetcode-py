# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.n_repeated_element_in_size_2n_array import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 2, 3, 3], 3),
        ([2, 1, 2, 5, 3, 2], 2),
        ([5, 1, 5, 2, 5, 3, 5, 4], 5),
    ],
)
def test_repeated_n_times(solution, nums, expected):
    actual = solution.repeatedNTimes(nums)
    assert expected == actual
