# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.find_k_th_smallest_pair_distance import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, k, expected',
    [
        ([1, 3, 1], 1, 0),
        ([1, 1, 1], 2, 0),
        ([1, 6, 1], 3, 5),
    ],
)
def test_smallest_distance_pari(solution, nums, k, expected):
    actual = solution.smallestDistancePair(nums, k)
    assert expected == actual
