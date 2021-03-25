# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.reverse_integer import Solution
    return Solution()


@pytest.mark.parametrize(
    'x,expected',
    [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
    ],
)
def test_zigzag_conversion(solution, x, expected):
    actual = solution.reverse(x)
    assert actual == expected
