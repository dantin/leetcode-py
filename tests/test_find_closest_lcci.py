# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.find_closest_lcci import Solution
    return Solution()


@pytest.mark.parametrize(
    'words, word1, word2, expected',
    [
        (['I', 'am', 'a', 'student', 'from', 'a', 'university', 'in', 'a', 'city'],
            'a', 'student', 1),
    ],
)
def test_find_closest(solution, words, word1, word2, expected):
    actual = solution.findClosest(words, word1, word2)
    assert expected == actual
