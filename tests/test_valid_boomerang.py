# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.valid_boomerang import Solution
    return Solution()


@pytest.mark.parametrize(
    'points, expected',
    [
        ([[1, 1], [2, 3], [3, 2]], True),
        ([[1, 1], [2, 2], [3, 3]], False),
    ],
)
def test_is_boomerang(solution, points, expected):
    actual = solution.isBoomerang(points)
    assert expected == actual
