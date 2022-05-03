# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.reorder_data_in_log_files import Solution
    return Solution()


@pytest.mark.parametrize(
    'logs, expected',
    [
        (['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'],
            ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']),
        (['a1 9 2 3 1', 'g1 act car', 'zo4 4 7', 'ab1 off key dog', 'a8 act zoo'],
            ['g1 act car', 'a8 act zoo', 'ab1 off key dog', 'a1 9 2 3 1', 'zo4 4 7']),
    ],
)
def test_reorder_log_files(solution, logs, expected):
    actual = solution.reorderLogFiles(logs)
    assert expected == actual
