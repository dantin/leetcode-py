# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.most_frequent_subtree_sum import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([5, 2, -3], [2, -3, 4]),
        ([5, 2, -5], [2]),
    ],
)
def test_find_frequent_sum(solution, nums, expected):
    from leetcode.utils.binary_search_tree import make_tree
    root = make_tree(nums, 0)
    actual = solution.findFrequentTreeSum(root)
    assert expected == actual
