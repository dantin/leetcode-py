# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.duplicate_zeros import Solution
    return Solution()


@pytest.mark.parametrize(
    'arr, expected',
    [
        ([1, 0, 2, 3, 0, 4, 5, 0], [1, 0, 0, 2, 3, 0, 0, 4]),
        ([1, 2, 3], [1, 2, 3]),
    ],
)
def test_duplicate_zeros(solution, arr, expected):
    actual = solution.duplicateZeros(arr)
    assert actual is None
    assert expected == arr
