# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for i in range(9)]
        columns = [{} for i in range(9)]
        boxes = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    k = (i // 3) * 3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    columns[j][num] = columns[j].get(num, 0) + 1
                    boxes[k][num] = boxes[k].get(num, 0) + 1
                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[k][num] > 1:
                        return False
        return True
