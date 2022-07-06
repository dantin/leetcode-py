# -*- coding: utf-8 -*-
from enum import Enum, auto
from collections import defaultdict


class ExprStatus(Enum):
    VALUE = auto()  # init state
    NONE = auto()   # unknown state
    LET = auto()    # let expression
    LET1 = auto()   # let expression finish vi variable
    LET2 = auto()   # let expression finish value expression
    ADD = auto()    # add expression
    ADD1 = auto()   # add expression finish e1
    ADD2 = auto()   # add expression finish e2
    MULT = auto()   # mult expression
    MULT1 = auto()  # mult expression finish e1
    MULT2 = auto()  # mult expression finish e2
    DONE = auto()   # complete


class Expr:
    __slots__ = 'status', 'var', 'value', 'e1', 'e2'

    def __init__(self, status):
        self.status = status
        self.var = ''   # variable in let
        self.value = 0  # value in let expression
        self.e1 = 0
        self.e2 = 0


class Solution:
    def evaluate(self, expression: str) -> int:
        scope = defaultdict(list)

        def calculate_token(token: str) -> int:
            return scope[token][-1] if token[0].islower() else int(token)

        variables = []
        stack = []
        cur = Expr(ExprStatus.VALUE)
        i, n = 0, len(expression)
        while i < n:
            # ignore space
            if expression[i] == ' ':
                i += 1
                continue

            if expression[i] == '(':
                i += 1
                stack.append(cur)
                cur = Expr(ExprStatus.NONE)
                continue
            if expression[i] == ')':
                i += 1
                if cur.status is ExprStatus.LET2:
                    token = str(cur.value)
                    for var in variables[-1]:
                        scope[var].pop()
                    variables.pop()
                elif cur.status is ExprStatus.ADD2:
                    token = str(cur.e1 + cur.e2)
                else:
                    token = str(cur.e1 * cur.e2)
                cur = stack.pop()
            else:
                i0 = i
                while i < n and expression[i] != ' ' and expression[i] != ')':
                    i += 1
                token = expression[i0:i]

            if cur.status is ExprStatus.VALUE:
                cur.value = int(token)
                cur.status = ExprStatus.DONE
            elif cur.status is ExprStatus.NONE:
                if token == 'let':
                    cur.status = ExprStatus.LET
                    variables.append([])
                elif token == 'add':
                    cur.status = ExprStatus.ADD
                elif token == 'mult':
                    cur.status = ExprStatus.MULT
            elif cur.status is ExprStatus.LET:
                if expression[i] == ')':
                    cur.value = calculate_token(token)
                    cur.status = ExprStatus.LET2
                else:
                    cur.var = token
                    variables[-1].append(token)
                    cur.status = ExprStatus.LET1
            elif cur.status is ExprStatus.LET1:
                scope[cur.var].append(calculate_token(token))
                cur.status = ExprStatus.LET
            elif cur.status is ExprStatus.ADD:
                cur.e1 = calculate_token(token)
                cur.status = ExprStatus.ADD1
            elif cur.status is ExprStatus.ADD1:
                cur.e2 = calculate_token(token)
                cur.status = ExprStatus.ADD2
            elif cur.status is ExprStatus.MULT:
                cur.e1 = calculate_token(token)
                cur.status = ExprStatus.MULT1
            elif cur.status is ExprStatus.MULT1:
                cur.e2 = calculate_token(token)
                cur.status = ExprStatus.MULT2
        return cur.value
