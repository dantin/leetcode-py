# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findDupicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for i in range(size):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [n for i, n in enumerate(nums) if n - 1 != i]
