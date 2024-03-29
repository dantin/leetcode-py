# -*- coding: utf-8 -*-
from typing import Tuple


class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp = [[False] * size for _ in range(size)]
        target = ''
        # n is the length of the current palindrome.
        for n in range(size):
            for i in range(size):
                # i, j represents two indexes of string.
                j = i + n
                if j >= size:
                    break

                if n == 0:
                    dp[i][j] = True
                elif n == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])

                # update longest palindrome.
                if dp[i][j] and n + 1 > len(target):
                    target = s[i:j + 1]
        return target

    def longestPalindrome2(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            lhs1, rhs1 = expand_at(s, i, i)
            lhs2, rhs2 = expand_at(s, i, i + 1)
            if rhs1 - lhs1 > end - start:
                start, end = lhs1, rhs1
            if rhs2 - lhs2 > end - start:
                start, end = lhs2, rhs2

        return s[start:end + 1]


def expand_at(s: str, left: int, right: int) -> Tuple[int, int]:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1
