# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.string_to_integer_atoi import Solution
    return Solution()


@pytest.mark.parametrize(
    'x,expected',
    [
        ('42', 42),
        ('   -42', -42),
        ('4193 with words', 4193),
        ('words and 987', 0),
        ('-91283472332', -2147483648),
    ],
)
def test_zigzag_conversion(solution, x, expected):
    actual = solution.myAtoi(x)
    assert actual == expected
