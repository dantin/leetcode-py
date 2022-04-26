# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = ['.'] * n

        def generate_board():
            board = []
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        def backtrace(row: int):
            if row == n:
                board = generate_board()
                solutions.append(board)
                return
            for i in range(n):
                if i in columns or (row - i) in diagonal1 or (row + i) in diagonal2:
                    continue

                queens[row] = i
                columns.add(i)
                diagonal1.add(row - i)
                diagonal2.add(row + i)
                backtrace(row + 1)
                columns.remove(i)
                diagonal1.remove(row - i)
                diagonal2.remove(row + i)

        solutions = []
        queens = [-1] * n
        columns = set()
        diagonal1, diagonal2 = set(), set()
        backtrace(0)
        return solutions
