# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.consecutive_numbers_sum import Solution
    return Solution()


@pytest.mark.parametrize(
    'n, expected',
    [
        (5, 2),
        (9, 3),
        (15, 4),
    ],
)
def test_consecutive_numbers_sum(solution, n, expected):
    actual = solution.consecutiveNumbersSum(n)
    assert expected == actual
