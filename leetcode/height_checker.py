# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        total = 0
        expected = sorted(heights)
        for lhs, rhs in zip(heights, expected):
            if lhs != rhs:
                total += 1
        return total
