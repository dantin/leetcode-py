# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.longest_substring_without_repeating_characters import Solution
    return Solution()


@pytest.mark.parametrize(
    's,expected',
    [
        ('abcabcbb', 3),
        ('bbbbb', 1),
        ('pwwkew', 3),
        (' ', 1),
    ],
)
def test_longest_substring_without_repeating_characters(solution, s, expected):
    actual = solution.lengthOfLongestSubstring(s)
    assert expected == actual
