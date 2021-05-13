# -*- coding: utf-8 -*-

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        cache = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                y = int(num2[j])
                cache[i + j + 1] += x * y
        for i in range(m + n - 1, 0, -1):
            cache[i - 1] += cache[i] // 10
            cache[i] %= 10

        i = 1 if cache[0] == 0 else 0
        return ''.join(str(x) for x in cache[i:])
