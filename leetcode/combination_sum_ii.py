# -*- coding: utf-8 -*-
import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, total: int) -> None:
            nonlocal nums
            if total == 0:
                combinations.append(nums[:])
                return
            if pos == len(freq) or total < freq[pos][0]:
                return

            dfs(pos + 1, total)

            count = min(total // freq[pos][0], freq[pos][1])
            for i in range(1, count + 1):
                nums.append(freq[pos][0])
                dfs(pos + 1, total - i * freq[pos][0])
            nums = nums[:-count]

        # freq is the sorted mapping of `(num, freq)`
        freq = sorted(collections.Counter(candidates).items())
        combinations = []
        nums = []
        dfs(0, target)
        return combinations
