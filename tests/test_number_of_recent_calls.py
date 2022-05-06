# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def counter():
    from leetcode.number_of_recent_calls import RecentCounter
    return RecentCounter()


@pytest.mark.parametrize(
    'commands, params, expected',
    [
        (['ping'] * 4, [[1], [100], [3001], [3002]], [1, 2, 3, 3]),
    ],
)
def test_ping(counter, commands, params, expected):
    actual = []
    for cmd, args in zip(commands, params):
        if cmd == 'ping':
            x = counter.ping(args[0])
            actual.append(x)
    assert expected == actual
