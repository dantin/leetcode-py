# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.binary_gap import Solution
    return Solution()


@pytest.mark.parametrize(
    'n, expected',
    [
        (22, 2),
        (8, 0),
        (5, 2),
    ],
)
def test_binary_gap(solution, n, expected):
    actual = solution.binaryGap(n)
    assert expected == actual
