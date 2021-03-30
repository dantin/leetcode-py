# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.roman_to_integer import Solution
    return Solution()


@pytest.mark.parametrize(
    'x,expected',
    [
        ('III', 3),
        ('IV', 4),
        ('IX', 9),
        ('LVIII', 58),
        ('MCMXCIV', 1994)
    ],
)
def test_roman_to_integer(solution, x, expected):
    actual = solution.romanToInt(x)
    assert actual == expected
