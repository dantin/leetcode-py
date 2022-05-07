# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.minimum_genetic_mutation import Solution
    return Solution()


@pytest.mark.parametrize(
    'start, end, bank, expected',
    [
        ('AACCGGTT', 'AACCGGTA', ['AACCGGTA'], 1),
        ('AACCGGTT', 'AAACGGTA', ['AACCGGTA', 'AACCGCTA', 'AAACGGTA'], 2),
        ('AAAAACCC', 'AACCCCCC', ['AAAACCCC', 'AAACCCCC', 'AACCCCCC'], 3),
    ],
)
def test_min_mutation(solution, start, end, bank, expected):
    actual = solution.minMutation(start, end, bank)
    assert expected == actual
