# -*- coding: utf-8 -*-

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_val = 0

        dp = [0 for _ in s]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    val = dp[i - 2] if i >= 2 else 0
                    dp[i] = val + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    val = dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0
                    dp[i] = dp[i - 1] + val + 2
                max_val = max(max_val, dp[i])

        return max_val
