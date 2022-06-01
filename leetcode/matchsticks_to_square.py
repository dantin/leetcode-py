# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        edge = total // 4

        dp = [-1] * (1 << len(matchsticks))
        dp[0] = 0
        for s in range(1, len(dp)):
            for k, v in enumerate(matchsticks):
                if s & (1 << k) == 0:
                    continue
                s1 = s & ~(1 << k)
                if dp[s1] >= 0 and dp[s1] + v <= edge:
                    dp[s] = (dp[s1] + v) % edge
                    break
        return dp[-1] == 0
