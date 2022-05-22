# -*- coding: utf-8 -*-
from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def dfs(candidates: int, total: int) -> bool:
            for i in range(maxChoosableInteger):
                if (candidates >> i) & 1 == 0:
                    if total + i + 1 >= desiredTotal:
                        return True
                    if not dfs(candidates | (1 << i), total + i + 1):
                        return True
            return False

        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        return dfs(0, 0)
