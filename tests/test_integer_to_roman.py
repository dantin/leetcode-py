# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.integer_to_roman import Solution
    return Solution()


@pytest.mark.parametrize(
    'x,expected',
    [
        (3, 'III'),
        (4, 'IV'),
        (9, 'IX'),
        (58, 'LVIII'),
        (1994, 'MCMXCIV')
    ],
)
def test_integer_to_roman(solution, x, expected):
    actual = solution.intToRoman(x)
    assert actual == expected
