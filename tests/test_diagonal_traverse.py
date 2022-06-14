# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.diagonal_traverse import Solution
    return Solution()


@pytest.mark.parametrize(
    'mat, expected',
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ],
)
def test_find_diagonal_order(solution, mat, expected):
    actual = solution.findDiagonalOrder(mat)
    assert expected == actual
