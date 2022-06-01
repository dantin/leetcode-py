# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.alien_dictionary import Solution
    return Solution()


@pytest.mark.parametrize(
    'words, expected',
    [
        (['wrt', 'wrf', 'er', 'ett', 'rftt'], 'wertf'),
        (['z', 'x'], 'zx'),
        (['z', 'x', 'z'], ''),
    ],
)
def test_binary_gap(solution, words, expected):
    actual = solution.alienOrder(words)
    assert expected == actual
