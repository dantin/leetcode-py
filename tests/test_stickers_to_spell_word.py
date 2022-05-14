# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.stickers_to_spell_word import Solution
    return Solution()


@pytest.mark.parametrize(
    'stickers, target, expected',
    [
        (['with', 'example', 'science'], 'thehat', 3),
        (['notice', 'possible'], 'basicbasic', -1),
    ],
)
def test_min_stickers(solution, stickers, target, expected):
    actual = solution.minStickers(stickers, target)
    assert expected == actual
