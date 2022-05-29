# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # notice shadow copy.
        rows = [[0] * 9 for _ in range(9)]
        columns = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == '.':
                    continue

                n = int(ch) - 1
                k = (i // 3) * 3 + j // 3

                rows[i][n] += 1
                columns[j][n] += 1
                boxes[k][n] += 1

                if rows[i][n] > 1 or columns[j][n] > 1 or boxes[k][n] > 1:
                    return False
        return True
