# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return [0]


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(f' Input: nums = {nums}')
    s = Solution()
    r = s.threeSum(nums)
    print(f' Output: {r}')
