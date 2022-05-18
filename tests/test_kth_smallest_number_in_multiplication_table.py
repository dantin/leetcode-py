# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.kth_smallest_number_in_multiplication_table import Solution
    return Solution()


@pytest.mark.parametrize(
    'm, n, k, expected',
    [
        (3, 3, 5, 3),
        (2, 3, 6, 6),
    ],
)
def test_find_kth_number(solution, m, n, k, expected):
    actual = solution.findKthNumber(m, n, k)
    assert expected == actual
