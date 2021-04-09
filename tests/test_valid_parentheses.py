# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.valid_parentheses import Solution
    return Solution()


@pytest.mark.parametrize(
    's,expected',
    [
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('([)]', False),
        ('{[]}', True),
    ],
)
def test_valid_parentheses(solution, s, expected):
    actual = solution.isValid(s)
    assert expected == actual
