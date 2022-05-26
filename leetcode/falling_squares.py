# -*- coding: utf-8 -*-
from typing import List, Tuple


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights = [0] * len(positions)
        for i, (l1, s1) in enumerate(positions):
            _, r1 = end_points(l1, s1)
            heights[i] = s1
            for j in range(i):
                l2, r2 = end_points(*positions[j])
                if r1 >= l2 and l1 <= r2:
                    heights[i] = max(heights[i], heights[j] + s1)
        for i in range(1, len(positions)):
            heights[i] = max(heights[i], heights[i - 1])
        return heights


def end_points(left: int, size: int, *args) -> Tuple[int, int]:
    right = left + size - 1
    return left, right
