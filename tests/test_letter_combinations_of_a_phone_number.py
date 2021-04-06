# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.letter_combinations_of_a_phone_number import Solution
    return Solution()


@pytest.mark.parametrize(
    'x,expected',
    [
        ('23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
        ('', []),
        ('2', ['a', 'b', 'c']),
    ],
)
def test_letter_combinations_of_a_phone_number(solution, x, expected):
    actual = solution.letterCombinations(x)
    assert actual == expected
