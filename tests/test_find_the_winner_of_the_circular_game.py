# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.find_the_winner_of_the_circular_game import Solution
    return Solution()


@pytest.mark.parametrize(
    'n, k, expected',
    [
        (5, 2, 3),
        (6, 5, 1),
    ],
)
def test_find_the_winner(solution, n, k, expected):
    actual = solution.findTheWinner(n, k)
    assert expected == actual
