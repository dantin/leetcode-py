# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates: List[int],
                begin: int, size: int,
                nums: List[int],
                target: int) -> None:
            if target < 0:
                return
            if target == 0:
                combinations.append(nums)
                return

            for i in range(begin, size):
                elem = candidates[i]
                dfs(candidates, i, size, nums + [elem], target - elem)

        size = len(candidates)
        if size == 0:
            return []
        combinations = []
        dfs(candidates, 0, size, [], target)
        return combinations
