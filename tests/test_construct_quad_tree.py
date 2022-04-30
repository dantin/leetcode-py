# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.construct_quad_tree import Solution
    return Solution()


@pytest.mark.parametrize(
    'grid, expected',
    [
        ([[0, 1], [1, 0]],
            [[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]),
        ([
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]],
            [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], 'null', 'null',
                'null', 'null', [1, 0], [1, 0], [1, 1], [1, 1]]),
        ([[1, 1], [1, 1]],
            [[1, 1]]),
        ([[0]],
            [[1, 0]]),
        ([
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]],
            [[0, 1], [1, 1], [1, 0], [1, 0], [1, 1]]),
    ],
)
def test_construct(solution, grid, expected):
    from leetcode.utils.quad_tree import dump
    root = solution.construct(grid)
    actual = dump(root)
    assert expected == actual
