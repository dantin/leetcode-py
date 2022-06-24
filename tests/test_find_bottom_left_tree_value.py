# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.find_bottom_left_tree_value import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([2, 1, 3], 1),
        ([1, 2, 3, 4, None, 5, 6, None, None, None, None, None, None, 7], 7),
    ],
)
def test_find_bottom_left_value(solution, nums, expected):
    from leetcode.utils.binary_search_tree import make_tree
    root = make_tree(nums, 0)
    actual = solution.findBottomLeftValue(root)
    assert expected == actual
