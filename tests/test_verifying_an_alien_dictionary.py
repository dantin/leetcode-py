# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.verifying_an_alien_dictionary import Solution
    return Solution()


@pytest.mark.parametrize(
    'words, order, expected',
    [
        (['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz', True),
        (['word', 'world', 'row'], 'worldabcefghijkmnpqstuvxyz', False),
        (['apple', 'app'], 'abcdefghijklmnopqrstuvwxyz', False),
    ],
)
def test_is_alien_sorted(solution, words, order, expected):
    actual = solution.isAlienSorted(words, order)
    assert expected == actual
