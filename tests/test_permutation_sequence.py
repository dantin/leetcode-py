# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.permutation_sequence import Solution
    return Solution()


@pytest.mark.parametrize(
    'n, k, expected',
    [
        (3, 3, '213'),
        (4, 9, '2314'),
        (3, 1, '123'),
    ],
)
def test_get_permutation(solution, n, k, expected):
    actual = solution.getPermutation(n, k)
    assert expected == actual
