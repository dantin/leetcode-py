# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        for i, jump in enumerate(nums):
            if k >= i and i + jump > k:
                k = i + jump
        return k >= i
