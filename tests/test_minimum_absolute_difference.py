# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.minimum_absolute_difference import Solution
    return Solution()


@pytest.mark.parametrize(
    'arr, expected',
    [
        ([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]),
    ],
)
def test_minimum_abs_difference(solution, arr, expected):
    actual = solution.minimumAbsDifference(arr)
    assert expected == actual
