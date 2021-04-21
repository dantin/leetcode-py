# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.next_permutation import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1], [1]),
    ],
)
def test_next_permutation(solution, nums, expected):
    solution.nextPermutation(nums)
    assert nums == expected
