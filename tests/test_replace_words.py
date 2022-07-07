# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.replace_words import Solution
    return Solution()


@pytest.mark.parametrize(
    'dictionary, sentence, expected',
    [
        (['cat', 'bat', 'rat'], 'the cattle was rattled by the battery',
            'the cat was rat by the bat'),
        (['a', 'b', 'c'], 'aadsfasf absbs bbab cadsfafs',
            'a a b c'),
    ],
)
def test_replace_words(solution, dictionary, sentence, expected):
    actual = solution.replaceWords(dictionary, sentence)
    assert expected == actual
