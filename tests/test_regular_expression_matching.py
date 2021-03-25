# -*- coding: utf-8 -*-

import pytest


@pytest.fixture
def solution():
    from leetcode.regular_expression_matching import Solution
    return Solution()


@pytest.mark.parametrize(
    'x,p,expected',
    [
        ('aa', 'a', False),
        ('aa', 'a*', True),
        ('ab', '.*', True),
        ('aab', 'c*a*b', True),
        ('mississippi', 'mis*is*p*.', False)
    ],
)
def test_regular_expression_matching(solution, x, p, expected):
    actual = solution.isMatch(x, p)
    assert actual == expected
