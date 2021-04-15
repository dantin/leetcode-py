# -*- coding: utf-8 -*-
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for pos, num in enumerate(nums):
            if num in cache and pos != cache[num]:
                return [pos, cache[num]]
            cache[target - num] = pos
        return []

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        # build vals using nums in <pos, val> pairs, which pos index is 0 and value is 1.
        vals = [(pos, num) for pos, num in enumerate(nums)]
        vals.sort(key=lambda x: x[1])  # sort nums by value.
        low, high = 0, len(vals) - 1
        while low < high:
            diff = target - vals[low][1]
            if diff > vals[high][1]:
                while low + 1 < high and vals[low][1] == vals[low + 1][1]:
                    low += 1
                low += 1
            elif diff < vals[high][1]:
                while high - 1 >= low and vals[high][1] == vals[high - 1][1]:
                    high -= 1
                high -= 1
            else:
                return [vals[low][0], vals[high][0]]
        return []
