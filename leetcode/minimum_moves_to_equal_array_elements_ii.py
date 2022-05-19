# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums) // 2]
        return sum(abs(n - mid) for n in nums)
