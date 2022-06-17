# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cache = {}
        for n in nums:
            if n in cache:
                cache[n] += 1
            else:
                cache[n] = 1

        total = 0

        for n, freq in cache.items():
            if k == 0:
                total += (freq >= 2)
            else:
                total += (n + k in cache)

        return total
