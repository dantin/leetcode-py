# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize(
    'params, expected',
    [
        ([[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
            [1, 1, 2, 3, 3, 3]),
    ],
)
def test_book(params, expected):
    from leetcode.my_calendar_iii import MyCalendarThree

    s = MyCalendarThree()
    actual = []
    for param in params:
        actual.append(s.book(*param))
    assert expected == actual
