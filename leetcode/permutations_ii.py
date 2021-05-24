# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        def backtrack(pos: int) -> None:
            if pos == len(nums):
                res.append(cache[:])
                return
            for i in range(len(nums)):
                if check[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and check[i - 1] == 0:
                    # choose all or choose none.
                    continue
                check[i] = 1
                cache.append(nums[i])
                backtrack(pos + 1)
                cache.pop()
                check[i] = 0

        res = []
        nums.sort()
        check = [0 for i in range(len(nums))]
        cache = []

        backtrack(0)

        return res
