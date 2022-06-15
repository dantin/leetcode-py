# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)

        def count(mid: int) -> int:
            right = 0
            cnt = 0
            for left in range(n):
                while right < n and nums[right] - nums[left] <= mid:
                    right += 1
                    cnt += right - left - 1
            return cnt

        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            r = count(mid)
            if r >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
