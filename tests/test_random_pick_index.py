# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize(
    'nums, target, expected',
    [
        ([1, 2, 3, 3, 3], 1, 0),
    ],
)
def test_add_two_numbers(nums, target, expected):
    from leetcode.random_pick_index import Solution
    s = Solution(nums)
    actual = s.pick(target)
    assert expected == actual
