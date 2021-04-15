# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.merge_two_sorted_lists import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums1,nums2,expected',
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ],
)
def test_merge_two_sorted_lists(solution, nums1, nums2, expected):
    from leetcode.utils.singly_linked_list import build, dump
    l1 = build(nums1)
    l2 = build(nums2)
    x = solution.mergeTwoLists(l1, l2)
    actual = dump(x)
    assert actual == expected
