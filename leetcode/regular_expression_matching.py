# -*- coding: utf-8 -*-

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True  # set init state
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    if matches(i, j - 1):
                        # copy of 's[j-1]' or ignore 'c*' completely.
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        # ignore 'c*' completely.
                        dp[i][j] = dp[i][j - 2]
                else:
                    if matches(i, j):
                        # normal match.
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]
