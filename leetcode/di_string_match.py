# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        perm = [0] * (n + 1)
        for i, ch in enumerate(s):
            if ch == 'I':
                perm[i] = low
                low += 1
            else:
                perm[i] = high
                high -= 1
        perm[n] = low
        return perm
