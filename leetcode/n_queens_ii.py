# -*- coding: utf-8 -*-

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrace(row: int) -> int:
            if row == n:
                return 1

            count = 0
            for col in range(n):
                if col in columns or row - col in diagonal1 or row + col in diagonal2:
                    continue
                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)
                count += backtrace(row + 1)
                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)
            return count

        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        return backtrace(0)
