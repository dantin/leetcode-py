# -*- coding: utf-8 -*-

class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        total = 0
        k = 1
        n *= 2
        while (k * k) < n:
            if n % k:
                k += 1
                continue
            if (n // k - (k - 1)) % 2 == 0:
                total += 1
            k += 1
        return total
