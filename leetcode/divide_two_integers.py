# -*- coding: utf-8 -*-

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2 ** 31, 2 ** 31 - 1
        flag = 1
        if dividend < 0:
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor = -flag, -divisor

        res = 0
        while dividend >= divisor:
            cur = divisor
            multiple = 1
            while cur + cur < dividend:
                cur += cur
                multiple += multiple
            dividend -= cur
            res += multiple

        res = res if flag > 0 else -res

        if res < MIN_INT:
            return MIN_INT
        elif MIN_INT <= res <= MAX_INT:
            return res
        else:
            return MAX_INT
