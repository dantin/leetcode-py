# -*- coding: utf-8 -*-
import math
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-math.inf] * n for _ in range(n)] for _ in range(n * 2 - 1)]
        dp[0][0][0] = grid[0][0]

        for k in range(1, n * 2 - 1):
            for x1 in range(max(k - n + 1, 0), min(k + 1, n)):
                y1 = k - x1
                if grid[x1][y1] == -1:
                    continue
                for x2 in range(x1, min(k + 1, n)):
                    y2 = k - x2
                    if grid[x2][y2] == -1:
                        continue
                    out = dp[k - 1][x1][x2]  # right
                    if x1:
                        out = max(out, dp[k - 1][x1 - 1][x2])  # down, right
                    if x2:
                        out = max(out, dp[k - 1][x1][x2 - 1])  # right, down
                    if x1 and x2:
                        out = max(out, dp[k - 1][x1 - 1][x2 - 1])  # down
                    out += grid[x1][y1]
                    if x2 != x1:  # avoid pickup the same cherry
                        out += grid[x2][y2]
                    dp[k][x1][x2] = out

        return max(dp[-1][-1][-1], 0)
