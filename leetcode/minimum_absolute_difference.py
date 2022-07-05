# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        size = len(arr)
        if size <= 1:
            return []

        arr.sort()
        output = []
        best = arr[size - 1] - arr[0]
        for i in range(0, size - 1):
            diff = arr[i + 1] - arr[i]
            if diff < best:
                best = diff
                output = [[arr[i], arr[i + 1]]]
            elif diff == best:
                output.append([arr[i], arr[i + 1]])
        return output
