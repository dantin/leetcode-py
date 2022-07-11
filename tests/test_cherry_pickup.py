# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.cherry_pickup import Solution
    return Solution()


@pytest.mark.parametrize(
    'grid, expected',
    [
        ([[0, 1, -1],
          [1, 0, -1],
          [1, 1, 1]], 5),
    ],
)
def test_cherry_pickup(solution, grid, expected):
    actual = solution.cherryPickup(grid)
    assert expected == actual
