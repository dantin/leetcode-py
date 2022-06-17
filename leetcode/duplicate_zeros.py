# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        j = k = len(arr) - 1
        while i <= j:
            if arr[i] == 0:
                if i == j:
                    arr[k] = 0
                    j, k = j - 1, k - 1
                    break
                j -= 1
            i += 1
        while j >= 0:
            if arr[j] == 0:
                arr[k] = 0
                k -= 1
            arr[k] = arr[j]
            j, k = j - 1, k - 1
