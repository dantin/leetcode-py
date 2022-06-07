# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.koko_eating_bananas import Solution
    return Solution()


@pytest.mark.parametrize(
    'piles, h, expected',
    [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ],
)
def test_min_eating_speed(solution, piles, h, expected):
    actual = solution.minEatingSpeed(piles, h)
    assert expected == actual
