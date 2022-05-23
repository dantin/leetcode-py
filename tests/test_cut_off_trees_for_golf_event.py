# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.cut_off_trees_for_golf_event import Solution
    return Solution()


@pytest.mark.parametrize(
    'forest, expected',
    [
        ([[1, 2, 3], [0, 0, 4], [7, 6, 5]], 6),
        ([[1, 2, 3], [0, 0, 0], [7, 6, 5]], -1),
    ],
)
def test_cut_off_tree(solution, forest, expected):
    actual = solution.cutOffTree(forest)
    assert expected == actual
