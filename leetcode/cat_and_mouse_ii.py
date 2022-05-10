# -*- coding: utf-8 -*-
from typing import List
from functools import lru_cache


_DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 'C':
                    cat = x, y
                elif grid[x][y] == 'F':
                    food = x, y
                elif grid[x][y] == 'M':
                    mouse = x, y
        print(f'{cat}, {mouse}, {food}')

        @lru_cache(None)
        def dfs(mouse, cat, i):
            if mouse == cat or cat == food or i > 128:
                return False
            if mouse == food:
                return True

            if i % 2:
                pos, jump = cat, catJump
                is_cat = True
            else:
                pos, jump = mouse, mouseJump
                is_cat = False

            for dx, dy in _DIRS:
                for jp in range(jump + 1):
                    nx, ny = pos[0] + dx * jp, pos[1] + dy * jp
                    if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] == '#':
                        break
                    if not is_cat and dfs((nx, ny), cat, i + 1):
                        return True
                    elif is_cat and not dfs(mouse, (nx, ny), i + 1):
                        return False
            return is_cat

        return dfs(mouse, cat, 0)
