# -*- coding: utf-8 -*-

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        retval = 0
        # dp[i] represents the longest valid parenthes ended by s[i].
        dp = [0] * len(s)

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    # previous is '(', match pattern '...()'.
                    pre = dp[i - 2] if i >= 2 else 0
                    dp[i] = pre + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    # previous is ')', match pattern '((...))'.
                    pre = dp[i - dp[i - 1] - 2] if (i - dp[i - 1]) >= 2 else 0
                    dp[i] = dp[i - 1] + pre + 2
                # update longest.
                retval = max(retval, dp[i])

        return retval
