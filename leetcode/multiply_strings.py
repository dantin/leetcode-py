# -*- coding: utf-8 -*-

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        product = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            x = ord(num1[i]) - ord('0')
            for j in range(n - 1, -1, -1):
                y = ord(num2[j]) - ord('0')
                product[i + j + 1] += x * y

        for i in range(m + n - 1, 0, -1):
            product[i - 1] += product[i] // 10
            product[i] %= 10

        i = 1 if product[0] == 0 else 0
        return ''.join(str(x) for x in product[i:])
