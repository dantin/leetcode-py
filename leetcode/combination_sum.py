# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(
            candidates: List[int],
            begin: int,
            end: int,
            nums: List[int],
            target: int,
        ) -> None:
            if target < 0:
                return
            if target == 0:
                retval.append(nums)
                return

            for i in range(begin, end):
                elem = candidates[i]
                dfs(candidates, i, end, nums + [elem], target - elem)

        size = len(candidates)
        if size == 0:
            return []
        retval = []
        dfs(candidates, 0, size, [], target)
        return retval
