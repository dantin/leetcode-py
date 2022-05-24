# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.univalued_binary_tree import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([1, 1, 1, 1, 1, None, 1], True),
        ([2, 2, 2, 5, 2], False),
    ],
)
def test_is_unival_tree(solution, nums, expected):
    from leetcode.utils.binary_search_tree import make_tree
    root = make_tree(nums, 0)
    actual = solution.isUnivalTree(root)
    assert expected == actual
