# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.longest_valid_parentheses import Solution
    return Solution()


@pytest.mark.parametrize(
    's,expected',
    [
        ('(()', 2),
        (')()())', 4),
        ('', 0),
        ('()(())', 6)
    ],
)
def test_longest_valid_parentheses(solution, s, expected):
    actual = solution.longestValidParentheses(s)
    assert expected == actual
