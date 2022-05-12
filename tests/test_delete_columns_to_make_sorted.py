# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.delete_columns_to_make_sorted import Solution
    return Solution()


@pytest.mark.parametrize(
    'strs, expected',
    [
        (['cba', 'daf', 'ghi'], 1),
        (['a', 'b'], 0),
        (['zyx', 'wvu', 'tsr'], 3),
    ],
)
def test_min_deletion_size(solution, strs, expected):
    actual = solution.minDeleteionSize(strs)
    assert expected == actual
