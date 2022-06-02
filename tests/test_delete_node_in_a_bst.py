# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.delete_node_in_a_bst import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, key, expected',
    [
        ([5, 3, 6, 2, 4, None, 7], 3, [5, 4, 6, 2, None, None, 7]),
        ([5, 3, 6, 2, 4, None, 7], 0, [5, 3, 6, 2, 4, None, 7]),
        ([], 0, []),
    ],
)
def test_binary_gap(solution, nums, key, expected):
    from leetcode.utils.binary_search_tree import make_tree, dump_tree
    root = make_tree(nums, 0)
    x = solution.deleteNode(root, key)
    actual = dump_tree(x)
    assert expected == actual
