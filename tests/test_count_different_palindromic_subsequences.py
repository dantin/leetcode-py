# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.count_different_palindromic_subsequences import Solution
    return Solution()


@pytest.mark.parametrize(
    's, expected',
    [
        ('bccb', 6),
        ('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba', 104860361),
    ],
)
def test_binary_gap(solution, s, expected):
    actual = solution.countPalindromicSubsequences(s)
    assert expected == actual
