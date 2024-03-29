# -*- coding: utf-8 -*-

class Solution:
    def reverse(self, x: int) -> int:
        negative = True if x < 0 else False
        if x < 0:
            x = -x

        n = 0
        while x > 0:
            n = n * 10
            # x, m = divmod(x, 10)
            # n += m
            n += x % 10
            x //= 10

        limit = 2 ** 31
        if negative:
            return -n if n <= limit else 0
        else:
            return n if n < limit else 0
