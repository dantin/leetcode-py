# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.subarray_product_less_than_k import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, k, expected',
    [
        ([10, 5, 2, 6], 100, 8),
        ([1, 2, 3], 0, 0),
    ],
)
def test_num_subarray_product_less_than_k(solution, nums, k, expected):
    actual = solution.numSubarrayProductLessThanK(nums, k)
    assert expected == actual
