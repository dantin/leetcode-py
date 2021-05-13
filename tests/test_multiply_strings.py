# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.multiply_strings import Solution
    return Solution()


@pytest.mark.parametrize(
    'num1,num2,expected',
    [
        ('2', '3', '6'),
        ('123', '456', '56088'),
    ],
)
def test_multiply_strings(solution, num1, num2, expected):
    actual = solution.multiply(num1, num2)
    assert actual == expected
