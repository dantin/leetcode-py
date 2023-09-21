# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums: List[int], target: int, left: bool) -> int:
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and nums[mid] == target):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        left = binary_search(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = binary_search(nums, target, False) - 1
        return [left, right]
