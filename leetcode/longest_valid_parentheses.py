# -*- coding: utf-8 -*-

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # '...()' extends valid parenthes.
                    pre = dp[i - 2] if i >= 2 else 0
                    dp[i] = pre + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    # '((...))' extends previous one.
                    pre = dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0
                    dp[i] = dp[i - 1] + pre + 2
                # update longest.
                longest = max(longest, dp[i])

        return longest
