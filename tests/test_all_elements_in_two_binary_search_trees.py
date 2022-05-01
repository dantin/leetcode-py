# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.all_elements_in_two_binary_search_trees import Solution
    return Solution()


@pytest.mark.parametrize(
    'num1, num2, expected',
    [
        ([2, 1, 4], [1, 0, 3], [0, 1, 1, 2, 3, 4]),
        ([1, None, 8], [8, 1], [1, 1, 8, 8]),
    ],
)
def test_get_all_elements(solution, num1, num2, expected):
    from leetcode.utils.binary_search_tree import make_tree
    root1 = make_tree(num1, 0)
    root2 = make_tree(num2, 0)
    actual = solution.getAllElements(root1, root2)
    assert expected == actual
