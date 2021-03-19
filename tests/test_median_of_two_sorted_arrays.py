# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.median_of_two_sorted_arrays import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums1,nums2,expected',
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
        ([], [1], 1.0),
        ([2], [], 2.0),
    ],
)
def test_two_sum_v1(solution, nums1, nums2, expected):
    actual = solution.findMedianSortedArrays(nums1, nums2)
    assert actual == expected
