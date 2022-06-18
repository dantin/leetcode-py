# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.sorted_cycle_linked_list import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, val, expected',
    [
        ([3, 4, 1], 2, [3, 4, 1, 2]),
        ([], 1, [1]),
        ([1], 0, [1, 0]),
    ],
)
def test_insert(solution, nums, val, expected):
    from leetcode.utils.cycle_linked_list import build, dump
    head = build(nums)
    x = solution.insert(head, val)
    actual = dump(x)
    assert expected == actual
