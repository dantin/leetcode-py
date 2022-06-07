# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(s: int) -> bool:
            count = 0
            for p in piles:
                d, m = divmod(p, s)
                count += d + (1 if m else 0)
            return count <= h

        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if not check(mid):
                left = mid + 1
            else:
                right = mid
        return left
