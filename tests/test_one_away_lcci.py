# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.one_way_lcci import Solution
    return Solution()


@pytest.mark.parametrize(
    'first, second, expected',
    [
        ('pale', 'ple', True),
        ('pales', 'pal', False),
    ],
)
def test_one_away_lcci(solution, first, second, expected):
    actual = solution.oneEditAway(first, second)
    assert expected == actual
