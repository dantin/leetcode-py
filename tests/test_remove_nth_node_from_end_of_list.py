# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.remove_nth_node_from_end_of_list import Solution
    return Solution()


@pytest.mark.parametrize(
    'head,n,expected',
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
    ],
)
def test_remove_nth_node_from_end_of_list(solution, head, n, expected):
    from leetcode.remove_nth_node_from_end_of_list import build_list, encode_list
    orig = build_list(head)
    node = solution.removeNthFromEnd(orig, n)
    actual = encode_list(node)
    assert actual == expected
