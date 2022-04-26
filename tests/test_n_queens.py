# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.n_queens import Solution
    return Solution()


@pytest.mark.parametrize(
    'n, expected',
    [
        (4, [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]),
        (1, [['Q']])
    ],
)
def test_n_queens(solution, n, expected):
    actual = solution.solveNQueens(n)
    assert expected == actual
