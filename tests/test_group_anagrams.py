# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.group_anagrams import Solution
    return Solution()


@pytest.mark.parametrize(
    'strs, expected',
    [
        (['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
            [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
        ([''], [['']]),
        (['a'], [['a']]),
    ],
)
def test_group_anagrams(solution, strs, expected):
    actual = solution.groupAnagrams(strs)
    assert actual == expected
