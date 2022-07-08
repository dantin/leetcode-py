# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd, even = 0, 0
        for n in position:
            if n % 2:
                odd += 1
            else:
                even += 1
        return min(odd, even)
