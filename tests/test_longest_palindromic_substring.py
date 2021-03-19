# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.longest_palindromic_substring import Solution
    return Solution()


@pytest.mark.parametrize(
    's,expected',
    [
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('a', 'a'),
        ('ac', 'a'),
    ],
)
def test_longest_palindromic_substring_v1(solution, s, expected):
    actual = solution.longestPalindrome(s)
    assert expected == actual


@pytest.mark.parametrize(
    's,expected',
    [
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('a', 'a'),
        ('ac', 'a'),
    ],
)
def test_longest_palindromic_substring_v2(solution, s, expected):
    actual = solution.longestPalindrome2(s)
    assert expected == actual
