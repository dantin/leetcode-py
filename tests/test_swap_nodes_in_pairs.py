# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.swap_nodes_in_pairs import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
    ],
)
def test_swap_nodes_in_pairs(solution, nums, expected):
    from leetcode.swap_nodes_in_pairs import make_list, dump_list
    head = make_list(nums)
    x = solution.swapPairs(head)
    actual = dump_list(x)
    assert actual == expected
