# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        def lcp(s1: str, s2: str) -> str:
            length, i = min(len(s1), len(s2)), 0
            while i < length and s1[i] == s2[i]:
                i += 1
            return s1[:i]

        prefix, size = strs[0], len(strs)
        for i in range(1, size):
            prefix = lcp(prefix, strs[i])
        return prefix

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if not strs:
            return ''
        length, size = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, size)):
                return strs[0][:i]
        return strs[0]

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        def lcp(start: int, end: int):
            if start == end:
                return strs[start]

            mid = (start + end) // 2
            left, right = lcp(start, mid), lcp(mid + 1, end)
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]

        return '' if not strs else lcp(0, len(strs) - 1)


if __name__ == '__main__':
    strs = ['flower', 'flow', 'flight']
    print(f' Input: strs = {strs}')
    s = Solution()
    r = s.longestCommonPrefix3(strs)
    print(f' Output: {r}')
