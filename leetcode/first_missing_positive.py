# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            if nums[i] <= 0:
                nums[i] = size + 1

        for i in range(size):
            n = abs(nums[i])
            if n <= size:
                nums[n - 1] = -abs(nums[n - 1])

        for i in range(size):
            if nums[i] > 0:
                return i + 1

        return size + 1
