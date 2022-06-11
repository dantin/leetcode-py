# -*- coding: utf-8 -*-

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp0 = dp1 = 0
        for ch in s:
            t0, t1 = dp0, min(dp0, dp1)
            if ch == '1':
                t0 += 1
            else:
                t1 += 1
            dp0, dp1 = t0, t1
        return min(dp0, dp1)
