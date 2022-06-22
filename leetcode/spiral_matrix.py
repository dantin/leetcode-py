# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])
        # count the layer
        layer = (min(m, n) + 1) // 2
        ans = []
        for i in range(layer):
            # left to right.
            for j in range(i, n - i):
                ans.append(matrix[i][j])
            # top to bottom.
            for j in range(i + 1, m - i):
                ans.append(matrix[j][n - i - 1])

            # right to left.
            if m - i - 1 != i:
                for j in range(n - i - 2, i - 1, -1):
                    ans.append(matrix[m - i - 1][j])

            # bottmo to top.
            if n - i - 1 != i:
                for j in range(m - i - 2, i, -1):
                    ans.append(matrix[j][i])

        return ans
