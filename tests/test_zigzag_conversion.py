# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.zigzag_conversion import Solution
    return Solution()


@pytest.mark.parametrize(
    's,row,expected',
    [
        ('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR'),
        ('PAYPALISHIRING', 4, 'PINALSIGYAHRPI'),
        ('A', 1, 'A'),
    ],
)
def test_zigzag_conversion(solution, s, row, expected):
    actual = solution.convert(s, row)
    assert actual == expected
