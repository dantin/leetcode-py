# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.spiral_matrix import Solution
    return Solution()


@pytest.mark.parametrize(
    'matrix, expected',
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ],
)
def test_spiral_order(solution, matrix, expected):
    actual = solution.spiralOrder(matrix)
    assert expected == actual
