# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(pos: int) -> None:
            if pos == n:
                permutation.append(nums[:])
                return
            for i in range(pos, n):
                nums[pos], nums[i] = nums[i], nums[pos]
                backtrack(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]

        n = len(nums)
        permutation = []
        backtrack(0)
        return permutation
