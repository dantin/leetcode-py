# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        dp = [[False] * size for _ in range(size)]
        target = ''
        # n + 1 is the length of the palindrome.
        for n in range(size):
            for i in range(size):
                j = i + n
                if j >= size:
                    break
                if n == 0:
                    dp[i][j] = True
                elif n == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and n + 1 > len(target):
                    target = s[i:j + 1]
        return target


if __name__ == '__main__':
    orig = 'badad'
    s = Solution()
    print(f' Input s = {orig}')
    o = s.longestPalindrome(orig)
    print(f' Output: {o}')
