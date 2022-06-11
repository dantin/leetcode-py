# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.flip_string_to_monotone_increasing import Solution
    return Solution()


@pytest.mark.parametrize(
    's, expected',
    [
        ('00110', 1),
        ('010110', 2),
        ('00011000', 2),
    ],
)
def test_min_flips_mono_incr(solution, s, expected):
    actual = solution.minFlipsMonoIncr(s)
    assert expected == actual
