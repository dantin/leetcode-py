# -*- coding: utf-8 -*-
import random
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x = x_center
        self.y = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(-self.r, self.r)
            y = random.uniform(-self.r, self.r)
            if x * x + y * y <= self.r * self.r:
                return [self.x + x, self.y + y]
