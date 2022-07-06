# -*- coding: utf-8 -*-
import pytest


@pytest.mark.parametrize(
    'params, expected',
    [
        ([[10, 20], [15, 25], [20, 30]],
            [True, False, True]),
    ],
)
def test_book(params, expected):
    from leetcode.my_calendar_i import MyCalendar

    s = MyCalendar()
    actual = []
    for param in params:
        actual.append(s.book(*param))
    assert expected == actual
