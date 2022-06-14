# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        if not mat[0]:
            return []

        m = len(mat)
        n = len(mat[0])

        nums = []
        flag = True
        for i in range(m + n):
            pm = m if flag else n
            pn = n if flag else m

            x = i if i < pm else pm - 1
            y = i - x

            while x >= 0 and y < pn:
                nums.append(mat[x][y] if flag else mat[y][x])
                x -= 1
                y += 1
            flag = not flag

        return nums

    def findDiagonalOrder2(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        if not mat[0]:
            return []

        m = len(mat)
        n = len(mat[0])

        nums = []
        i = 0
        while i < m + n:
            # 1, 3, 5...
            x1 = i if i < m else m - 1
            y1 = i - x1
            while x1 >= 0 and y1 < n:
                nums.append(mat[x1][y1])
                x1 -= 1
                y1 += 1
            i += 1

            if i >= m + n:
                break

            # 2, 4, 6
            y2 = i if i < n else n - 1
            x2 = i - y2
            while y2 >= 0 and x2 < m:
                nums.append(mat[x2][y2])
                x2 += 1
                y2 -= 1
            i += 1

        return nums
