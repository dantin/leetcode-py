# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        return 0


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f' Input: {height}')
    s = Solution()
    r = s.maxArea(height)
    print(f' Output: {r}')
