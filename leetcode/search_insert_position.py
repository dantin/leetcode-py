# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        x = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                x = mid
                right = mid - 1
            else:
                left = mid + 1

        return x
