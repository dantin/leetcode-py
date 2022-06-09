# -*- coding: utf-8 -*-
from bisect import bisect_right
from random import randrange
from typing import List


class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sum = [0]
        for a, b, x, y in rects:
            self.sum.append(self.sum[-1] + (x - a + 1) * (y - b + 1))

    def pick(self) -> List[int]:
        k = randrange(self.sum[-1])
        rect_idx = bisect_right(self.sum, k) - 1
        a, b, _, y = self.rects[rect_idx]
        delta_a, delta_b = divmod(k - self.sum[rect_idx], y - b + 1)
        return [a + delta_a, b + delta_b]
