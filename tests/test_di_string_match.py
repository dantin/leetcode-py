# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.di_string_match import Solution
    return Solution()


@pytest.mark.parametrize(
    's, expected',
    [
        ('IDID', [0, 4, 1, 3, 2]),
        ('III', [0, 1, 2, 3]),
        ('DDI', [3, 2, 0, 1]),
    ],
)
def test_di_string_match(solution, s, expected):
    actual = solution.diStringMatch(s)
    assert expected == actual
