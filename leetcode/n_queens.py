# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = ['.'] * n

        def generate_board():
            board = []
            for i in range(n):
                # i represents row index.
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board

        def backtrace(row: int):
            if row == n:
                board = generate_board()
                solutions.append(board)
                return
            for col in range(n):
                if col in columns or (row - col) in diagonal1 or (row + col) in diagonal2:
                    continue

                queens[row] = col
                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)
                backtrace(row + 1)
                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        solutions = []
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        backtrace(0)
        return solutions
