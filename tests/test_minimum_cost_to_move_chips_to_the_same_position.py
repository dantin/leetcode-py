# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.minimum_cost_to_move_chips_to_the_same_position import Solution
    return Solution()


@pytest.mark.parametrize(
    'position, expected',
    [
        ([1, 2, 3], 1),
        ([2, 2, 2, 3, 3], 2),
        ([1, 1000000000], 1),
    ],
)
def test_min_cost_to_move_chips(solution, position, expected):
    actual = solution.minCostToMoveChips(position)
    assert expected == actual
