# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.powx_n import Solution
    return Solution()


@pytest.mark.parametrize(
    'x, n, expected',
    [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
    ],
)
def test_my_pow(solution, x, n, expected):
    actual = solution.myPow(x, n)
    assert actual == pytest.approx(expected)
