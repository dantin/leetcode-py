# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        k1 = (points[1][1] - points[0][1]) * (points[2][0] - points[0][0])
        k2 = (points[2][1] - points[0][1]) * (points[1][0] - points[0][0])
        return k1 != k2
