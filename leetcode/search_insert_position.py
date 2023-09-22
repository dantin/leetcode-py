# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1

        return lo
