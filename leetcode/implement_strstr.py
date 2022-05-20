# -*- coding: utf-8 -*-
from typing import Dict


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def init_shift(s: str) -> Dict[str, int]:
            steps = {}
            for i in range(len(s) - 1, -1, -1):
                if s[i] not in steps:
                    steps[s[i]] = len(s) - i
            steps['out'] = len(s) + 1
            return steps

        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0

        steps = init_shift(needle)
        i = 0
        while i + len(needle) <= len(haystack):
            target = haystack[i:i + len(needle)]
            if target == needle:
                return i

            if i + len(needle) >= len(haystack):
                return -1

            ch = haystack[i + len(needle)]
            if ch in steps:
                i += steps[ch]
            else:
                i += steps['out']
        return -1 if i + len(needle) >= len(haystack) else i
