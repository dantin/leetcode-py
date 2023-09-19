# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}  # window represents a sliding window which contains char and its last position.
        retval = 0   # retval is the length of longest substring.
        length = 0   # length is the length of current substring.
        i = 0

        while i < len(s):
            c = s[i]
            if c not in window:
                window[c] = i
                length += 1
                i += 1
            else:
                retval = max(retval, length)
                i = window[c] + 1
                length = 0
                window = {}

        return max(retval, length)
