# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize(
    'radius, x, y',
    [
        (1.0, 0.0, 0.0),
    ],
)
def test_rand_point(radius, x, y):
    from leetcode.generate_random_point_in_a_circle import Solution

    solution = Solution(radius, x, y)
    actual_x, actual_y = solution.randPoint()
    assert actual_x * actual_x + actual_y * actual_y <= 1.0
