# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1

        if i < 0:
            return 0

        end = i
        while i >= 0 and s[i] != ' ':
            i -= 1

        return end - i
