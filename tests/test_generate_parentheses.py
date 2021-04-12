# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.generate_parentheses import Solution
    return Solution()


@pytest.mark.parametrize(
    'n, expected',
    [
        (3, ['((()))', '(()())', '(())()', '()(())', '()()()']),
        (1, ['()'])
    ],
)
def test_generate_parentheses(solution, n, expected):
    actual = solution.generateParenthesis(n)
    assert actual == expected
