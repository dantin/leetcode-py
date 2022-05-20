# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        # find first unordered num.
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            # find last num bigger than the unordered num.
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            # swap them.
            nums[i], nums[j] = nums[j], nums[i]

        # reorder s[i + 1:]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
