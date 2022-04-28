# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        size = len(nums)
        begin, end = 0, size - 1
        while begin < end:
            while begin < size and nums[begin] % 2 == 0:
                begin += 1
            while end >= 0 and nums[end] % 2 == 1:
                end -= 1
            if begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
                end -= 1
        return nums
