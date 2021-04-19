# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.implement_strstr import Solution
    return Solution()


@pytest.mark.parametrize(
    'haystack,needle,expected',
    [
        ('hello', 'll', 2),
        ('aaaaa', 'bba', -1),
        ('', '', 0),
    ],
)
def test_implement_strstr(solution, haystack, needle, expected):
    actual = solution.strStr(haystack, needle)
    assert actual == expected
