# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.palindrome_number import Solution
    return Solution()


@pytest.mark.parametrize(
    'x,expected',
    [
        (121, True),
        (-121, False),
        (10, False),
        (-101, False),
        (0, True),
    ],
)
def test_palindrome_number(solution, x, expected):
    actual = solution.isPalindrome(x)
    assert actual == expected
