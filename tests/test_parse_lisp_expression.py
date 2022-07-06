# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.parse_lisp_expression import Solution
    return Solution()


@pytest.mark.parametrize(
    'expression, expected',
    [
        ('(let x 2 (mult x (let x 3 y 4 (add x y))))', 14),
        ('(let x 3 x 2 x)', 2),
        ('(let x 1 y 2 x (add x y) (add x y))', 5),
    ],
)
def test_evaluate(solution, expression, expected):
    actual = solution.evaluate(expression)
    assert expected == actual
