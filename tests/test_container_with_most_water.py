# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.container_with_most_water import Solution
    return Solution()


@pytest.mark.parametrize(
    'height,expected',
    [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
    ],
)
def test_container_with_most_water(solution, height, expected):
    actual = solution.maxArea(height)
    assert actual == expected
