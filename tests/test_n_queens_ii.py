# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.n_queens_ii import Solution
    return Solution()


@pytest.mark.parametrize(
    'n, expected',
    [
        (4, 2),
        (1, 1),
    ],
)
def test_total_n_queens(solution, n, expected):
    actual = solution.totalNQueens(n)
    assert expected == actual
