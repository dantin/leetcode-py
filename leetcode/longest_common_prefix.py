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

    def longestCommonPrefix4(self, strs: List[str]) -> str:
        def is_common_prefix(length):
            s0, size = strs[0][:length], len(strs)
            return all(strs[i][:length] == s0 for i in range(1, size))

        if not strs:
            return ''

        min_len = min(len(s) for s in strs)
        low, high = 0, min_len
        while low < high:
            mid = (high - low + 1) // 2 + low
            if is_common_prefix(mid):
                low = mid
            else:
                high = mid - 1
        return strs[0][:low]
