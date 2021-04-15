# -*- coding: utf-8 -*-

class Solution:
    def reverse(self, x: int) -> int:
        is_neg = True if x < 0 else False
        if x < 0:
            x = -x

        n, limit = 0, 2 ** 31
        while x > 0:
            n = n * 10
            n += x % 10
            x //= 10
        if is_neg:
            return -n if n <= limit else 0
        else:
            return n if n < limit else 0
