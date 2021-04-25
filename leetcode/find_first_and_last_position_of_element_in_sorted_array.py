# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums: List[int], target: int, lower: bool) -> int:
            left, right = 0, len(nums) - 1
            x = len(nums)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target or (lower and nums[mid] >= target):
                    right = mid - 1
                    x = mid
                else:
                    left = mid + 1
            return x

        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False) - 1
        if left <= right and right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]
