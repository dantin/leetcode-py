# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        diff = max(nums) - min(nums) - 2 * k
        return 0 if diff < 0 else diff
