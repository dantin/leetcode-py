# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.add_two_numbers import Solution
    return Solution()


@pytest.mark.parametrize(
    'num1,num2,expected',
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
    ],
)
def test_add_two_numbers(solution, num1, num2, expected):
    from leetcode.add_two_numbers import make_node
    n1 = make_node(num1)
    n2 = make_node(num2)
    node = solution.addTwoNumbers(n1, n2)
    actual = []
    while node:
        actual.append(node.val)
        node = node.next
    assert len(expected) == len(actual)
    assert all([a == b for a, b in zip(actual, expected)])
