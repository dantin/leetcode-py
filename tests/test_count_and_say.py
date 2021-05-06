# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.count_and_say import Solution
    return Solution()


@pytest.mark.parametrize(
    'n,expected',
    [
        (1, '1'),
        (2, '11'),
        (3, '21'),
        (4, '1211'),
    ],
)
def test_count_and_say(solution, n, expected):
    actual = solution.countAndSay(n)
    assert actual == expected
