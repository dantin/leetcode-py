# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        area = 0.0
        size = len(points)
        for i in range(size - 2):
            for j in range(i + 1, size - 1):
                for k in range(i + 2, size):
                    (x1, y1), (x2, y2), (x3, y3) = points[i], points[j], points[k]
                    a = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
                    area = max(area, a)
        return area
