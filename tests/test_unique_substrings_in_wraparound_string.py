# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.unique_substrings_in_wraparound_string import Solution
    return Solution()


@pytest.mark.parametrize(
    'p, expected',
    [
        ('a', 1),
        ('cac', 2),
        ('zab', 6),
    ],
)
def test_find_substring_in_wrapround_string(solution, p, expected):
    actual = solution.findSubstringInWraproundString(p)
    assert expected == actual
