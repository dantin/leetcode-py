# -*- coding: utf-8 -*-

class Solution:
    def binaryGap(self, n: int) -> int:
        gap = 0
        i, last = 0, -1
        while n:
            if n & 1:
                if last != -1:
                    gap = max(gap, i - last)
                last = i
            n >>= 1
            i += 1

        return gap
