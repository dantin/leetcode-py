# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.jump_game_ii import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,expected',
    [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
    ],
)
def test_jump_game_ii(solution, nums, expected):
    actual = solution.jump(nums)
    assert actual == expected
