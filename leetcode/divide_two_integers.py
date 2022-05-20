# -*- coding: utf-8 -*-

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2 ** 31, 2 ** 31 - 1

        flag = 1
        if dividend < 0:
            flag, dividend = -flag, -dividend
        if divisor < 0:
            flag, divisor = -flag, -divisor

        quotient = 0
        while dividend >= divisor:
            c = divisor
            multiple = 1
            while c + c < dividend:
                c += c
                multiple += multiple
            dividend -= c
            quotient += multiple

        quotient = quotient if flag > 0 else -quotient

        if quotient < MIN_INT:
            return MIN_INT
        if quotient > MAX_INT:
            return MAX_INT

        return quotient
