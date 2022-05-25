# -*- coding: utf-8 -*-
from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        count = defaultdict(int)
        k = 0
        for i, ch in enumerate(p):
            if i > 0 and (ord(ch) - ord(p[i - 1])) % 26 == 1:
                k += 1
            else:
                k = 1
            count[ch] = max(k, count[ch])
        return sum(count.values())
