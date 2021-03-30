# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.longest_common_prefix import Solution
    return Solution()


@pytest.mark.parametrize(
    'strs,expected',
    [
        (['flower', 'flow', 'flight'], 'fl'),
        (['dog', 'racecar', 'car'], '')
    ],
)
def test_longest_common_prefix(solution, strs, expected):
    actual = solution.longestCommonPrefix(strs)
    assert actual == expected
    actual = solution.longestCommonPrefix2(strs)
    assert actual == expected
    actual = solution.longestCommonPrefix3(strs)
    assert actual == expected
