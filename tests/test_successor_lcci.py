# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.successor_lcci import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, p, expected',
    [
        ([2, 1, 3], 1, 2),
        ([5, 3, 6, 2, 4, None, None, 1], 6, None),
    ],
)
def test_inorder_successor(solution, nums, p, expected):
    from leetcode.utils.binary_search_tree import make_tree, find_node

    root = make_tree(nums, 0)
    target = find_node(root, p)
    actual = solution.inorderSucessor(root, target)
    if actual:
        assert expected == actual.val
    else:
        assert expected == actual
