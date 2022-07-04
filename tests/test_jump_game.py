# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.jump_game import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ],
)
def test_can_jump(solution, nums, expected):
    actual = solution.canJump(nums)
    assert expected == actual
