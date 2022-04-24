# -*- coding: utf-8 -*-

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quick_multiply(n: int) -> float:
            y = 1.0
            exp = x
            while n > 0:
                if n % 2 == 1:
                    y *= exp
                exp *= exp
                n //= 2

            return y

        if n >= 0:
            return quick_multiply(n)

        return 1.0 / quick_multiply(-n)
