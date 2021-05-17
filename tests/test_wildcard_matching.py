# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.wildcard_matching import Solution
    return Solution()


@pytest.mark.parametrize(
    's,p,expected',
    [
        ('aa', 'a', False),
        ('aa', '*', True),
        ('cb', '?a', False),
        ('adceb', '*a*b', True),
        ('acdcb', 'a*c?b', False),
    ],
)
def test_wildcard_matching(solution, s, p, expected):
    actual = solution.isMatch(s, p)
    assert actual == expected
