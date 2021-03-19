# -*- coding: utf-8 -*-

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return s


if __name__ == '__main__':
    orig = 'badad'
    s = Solution()
    print(f' Input s = {orig}')
    o = s.longestPalindrome(orig)
    print(f' Output: {o}')
