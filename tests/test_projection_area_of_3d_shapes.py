# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.projection_area_of_3d_shapes import Solution
    return Solution()


@pytest.mark.parametrize(
    'grid, expected',
    [
        ([[1, 2], [3, 4]], 17),
        ([[2]], 5),
        ([[1, 0], [0, 2]], 8),
    ],
)
def test_binary_gap(solution, grid, expected):
    actual = solution.projectionArea(grid)
    assert expected == actual
