# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(
            begin: int,
            end: int,
            nums: List[int],
            target: int
        ) -> None:
            if target == 0:
                retval.append(nums[:])
                return
            if target < 0:
                return

            i = begin
            while i < end:
                n = candidates[i]
                nums.append(n)
                dfs(i + 1, end, nums, target - n)
                nums.pop()
                while i < end - 1 and n == candidates[i + 1]:
                    i += 1
                i += 1

        retval = []
        if len(candidates) == 0 and target < 0:
            return retval
        candidates = sorted(candidates)
        nums = []
        dfs(0, len(candidates), nums, target)
        return retval
