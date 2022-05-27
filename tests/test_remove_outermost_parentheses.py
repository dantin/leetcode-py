# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.remove_outermost_parentheses import Solution
    return Solution()


@pytest.mark.parametrize(
    's, expected',
    [
        ('(()())(())', '()()()'),
        ('(()())(())(()(()))', '()()()()(())'),
        ('()()', ''),
    ],
)
def test_remove_outer_parentheses(solution, s, expected):
    actual = solution.removeOuterParentheses(s)
    assert expected == actual
