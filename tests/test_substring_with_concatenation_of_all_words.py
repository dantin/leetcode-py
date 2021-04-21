# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.substring_with_concatenation_of_all_words import Solution
    return Solution()


@pytest.mark.parametrize(
    's,words,expected',
    [
        ('barfoothefoobarman', ['foo', 'bar'], [0, 9]),
        ('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'word'], []),
        ('barfoofoobarthefoobarman', ['bar', 'foo', 'the'], [6, 9, 12]),
    ],
)
def test_substring_with_concatenation_of_all_words(solution, s, words, expected):
    actual = solution.findSubstring(s, words)
    assert actual == expected
