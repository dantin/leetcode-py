# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cache = set()
        for n in nums:
            if n in cache:
                return n
            cache.add(n)

        return -1
