# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.sum_of_root_to_leaf_binary_numbers import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 0, 1, 0, 1, 0, 1], 22),
        ([0], 0),
    ],
)
def test_sum_root_to_leaf(solution, nums, expected):
    from leetcode.utils.binary_search_tree import make_tree
    root = make_tree(nums, 0)
    actual = solution.sumRootToLeaf(root)
    assert expected == actual
