# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        size = len(height)

        left_max = [height[0]] + [0] * (size - 1)
        for i in range(1, size):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0] * (size - 1) + [height[size - 1]]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total = sum(min(left_max[i], right_max[i]) - height[i] for i in range(size))
        return total
