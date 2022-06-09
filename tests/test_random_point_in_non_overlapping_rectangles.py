# -*- coding: utf-8 -*-
import pytest

from leetcode.random_point_in_non_overlapping_rectangles import Solution


@pytest.mark.parametrize(
    'cmds, params',
    [
        (['Solution', 'pick', 'pick', 'pick', 'pick', 'pick'],
            [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]),
    ],
)
def test_pick(cmds, params):
    solution = Solution(*params[0])
    for cmd, param in zip(cmds, params):
        if cmd == 'pick':
            x = solution.pick()
            assert len(x) > 0
