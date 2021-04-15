# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.reverse_nodes_in_k_group import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,k,expected',
    [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ([1], 1, [1]),
    ],
)
def test_reverse_nodes_in_k_group(solution, nums, k, expected):
    from leetcode.reverse_nodes_in_k_group import make_list, dump_list
    x = make_list(nums)
    head = solution.reverseKGroup(x, k)
    actual = dump_list(head)
    assert actual == expected
