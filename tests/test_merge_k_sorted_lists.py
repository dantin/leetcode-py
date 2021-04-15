# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.merge_k_sorted_lists import Solution
    return Solution()


@pytest.mark.parametrize(
    'lists,expected',
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
    ],
)
def test_merge_two_sorted_lists(solution, lists, expected):
    from leetcode.utils.singly_linked_list import build, dump
    x = []
    for nums in lists:
        head = build(nums)
        x.append(head)
    head = solution.mergeKLists(x)
    actual = dump(head)
    assert actual == expected

    x = []
    for nums in lists:
        head = build(nums)
        x.append(head)

    head = solution.mergeKLists2(x)
    actual = dump(head)
    assert actual == expected
