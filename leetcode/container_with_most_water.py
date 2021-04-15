# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lhs, rhs = 0, len(height) - 1
        max_area = 0
        while lhs < rhs:
            area = min(height[lhs], height[rhs]) * (rhs - lhs)
            max_area = max(area, max_area)
            if height[lhs] <= height[rhs]:
                lhs += 1
            else:
                rhs -= 1
        return max_area
