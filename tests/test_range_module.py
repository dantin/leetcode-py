# -*- coding: utf-8 -*-
import pytest

from leetcode.range_module import RangeModule


@pytest.mark.parametrize(
    'cmds, params, expected',
    [
        (['RangeModule', 'addRange', 'removeRange', 'queryRange', 'queryRange', 'queryRange'],
            [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]],
            [None, None, None, True, False, True]),
    ],
)
def test_range_module(cmds, params, expected):
    s = RangeModule()

    output = [None]
    for cmd, param in zip(cmds, params):
        if cmd == 'addRange':
            x = s.addRange(*param)
        elif cmd == 'removeRange':
            x = s.removeRange(*param)
        elif cmd == 'queryRange':
            x = s.queryRange(*param)
        else:
            continue
        output.append(x)

    assert expected == output
