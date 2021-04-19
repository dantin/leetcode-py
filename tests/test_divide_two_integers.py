# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.divide_two_integers import Solution
    return Solution()


@pytest.mark.parametrize(
    'dividend,divisor,expected',
    [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
    ],
)
def test_divide_two_integers(solution, dividend, divisor, expected):
    actual = solution.divide(dividend, divisor)
    assert actual == expected
