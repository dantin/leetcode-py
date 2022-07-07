# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.length_of_last_word import Solution
    return Solution()


@pytest.mark.parametrize(
    's, expected',
    [
        ('Hello World', 5),
        ('   fly me   to  the moon ', 4),
        ('luffy is still joyboy', 6),
    ],
)
def test_length_of_last_word(solution, s, expected):
    actual = solution.lengthOfLastWord(s)
    assert expected == actual
