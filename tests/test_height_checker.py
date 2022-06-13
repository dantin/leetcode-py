# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.height_checker import Solution
    return Solution()


@pytest.mark.parametrize(
    'heights, expected',
    [
        ([1, 1, 4, 2, 1, 3], 3),
        ([5, 1, 2, 3, 4], 5),
        ([1, 2, 3, 4, 5], 0),
    ],
)
def test_height_checker(solution, heights, expected):
    actual = solution.heightChecker(heights)
    assert expected == actual
