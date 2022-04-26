# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top = sum(1 for obj in grid for v in obj if v > 0)
        left = sum(map(max, zip(*grid)))
        front = sum(map(max, grid))
        return top + left + front
