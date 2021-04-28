# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def dfs(pos: int) -> None:
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            for digit in range(9):
                if ((not lines[i][digit]) and
                        (not columns[j][digit]) and
                        (not boxes[i // 3][j // 3][digit])):
                    lines[i][digit] = columns[j][digit] = boxes[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    lines[i][digit] = columns[j][digit] = boxes[i // 3][j // 3][digit] = False
                if valid:
                    return

        lines = [[False] * 9 for _ in range(9)]
        columns = [[False] * 9 for _ in range(9)]
        boxes = [[[False] * 9 for _i in range(3)] for _j in range(3)]
        valid = False
        spaces = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j]) - 1
                    lines[i][digit] = columns[j][digit] = boxes[i // 3][j // 3][digit] = True

        dfs(0)
