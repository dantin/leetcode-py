# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.pacific_atlantic_water_flow import Solution
    return Solution()


@pytest.mark.parametrize(
    'heights, expected',
    [
        ([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]],
            [[4, 0], [0, 4], [3, 1], [1, 4], [3, 0], [2, 2], [1, 3]]),
        ([[2, 1], [1, 2]],
            [[1, 0], [0, 1], [1, 1], [0, 0]])
    ],
)
def test_pacific_atlantic(solution, heights, expected):
    actual = solution.pacificAtlantic(heights)
    assert expected == actual
