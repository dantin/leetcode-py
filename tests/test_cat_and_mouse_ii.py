# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.cat_and_mouse_ii import Solution
    return Solution()


@pytest.mark.parametrize(
    'grid, catJump, mouseJump, expected',
    [
        (['####F', '#C...', 'M....'], 1, 2, True),
        (['M.C...F'], 1, 4, True),
        (['M.C...F'], 1, 3, False),
        (['C...#', '...#F', '....#', 'M....'], 2, 5, False),
        (['.M...', '..#..', '#..#.', 'C#.#.', '...#F'], 3, 1, True),
    ],
)
def test_can_mouse_win(solution, grid, catJump, mouseJump, expected):
    actual = solution.canMouseWin(grid, catJump, mouseJump)
    assert expected == actual
