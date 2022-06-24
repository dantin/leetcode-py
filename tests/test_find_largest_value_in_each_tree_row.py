# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.find_largest_value_in_each_tree_row import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 3, 2, 5, 3, None, 9], [1, 3, 9]),
        ([1, 2, 3], [1, 3]),
    ],
)
def test_largest_values(solution, nums, expected):
    from leetcode.utils.binary_search_tree import make_tree
    root = make_tree(nums, 0)
    actual = solution.largestValues(root)
    assert expected == actual
