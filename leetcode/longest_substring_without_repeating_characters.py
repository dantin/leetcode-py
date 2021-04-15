# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = {}
        max_len, length = 0, 0
        i = 0
        while i < len(s):
            c = s[i]
            if c not in cache:
                cache[c] = i
                length += 1
                i += 1
            else:
                max_len = max(max_len, length)
                length = 0
                i = cache[c] + 1
                cache = {}

        max_len = max(max_len, length)
        return max_len
