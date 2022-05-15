# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.largest_triangle_area import Solution
    return Solution()


@pytest.mark.parametrize(
    'points, expected',
    [
        ([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2.0),
    ],
)
def test_largest_triangle_area(solution, points, expected):
    actual = solution.largestTriangleArea(points)
    assert expected == actual
