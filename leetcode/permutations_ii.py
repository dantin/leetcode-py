# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        def backtrack(pos: int) -> None:
            if pos == len(nums):
                permutations.append(cache[:])
                return
            for i in range(len(nums)):
                if check[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not check[i - 1]:
                    # choose all or choose none.
                    continue

                check[i] = True
                cache.append(nums[i])
                backtrack(pos + 1)
                cache.pop()
                check[i] = False

        nums.sort()
        check = [False] * len(nums)

        permutations = []
        cache = []

        backtrack(0)

        return permutations
