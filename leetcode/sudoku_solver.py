# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(pos: int) -> None:
            nonlocal done
            if pos == len(spaces):
                done = True
                return

            i, j = spaces[pos]
            k = (i // 3) * 3 + j // 3
            for digit in range(9):
                if ((not rows[i][digit]) and
                        (not columns[j][digit]) and
                        (not boxes[k][digit])):
                    rows[i][digit] = columns[j][digit] = boxes[k][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    rows[i][digit] = columns[j][digit] = boxes[k][digit] = False
                if done:
                    return

        rows = [[False] * 9 for _ in range(9)]
        columns = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]
        done = False
        spaces = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    k = (i // 3) * 3 + j // 3
                    rows[i][digit] = columns[j][digit] = boxes[k][digit] = True

        dfs(0)
