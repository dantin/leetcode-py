# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.falling_squares import Solution
    return Solution()


@pytest.mark.parametrize(
    'positions, expected',
    [
        ([[1, 2], [2, 3], [6, 1]], [2, 5, 5]),
        ([[100, 100], [200, 100]], [100, 100]),
    ],
)
def test_falling_squares(solution, positions, expected):
    actual = solution.fallingSquares(positions)
    assert expected == actual
