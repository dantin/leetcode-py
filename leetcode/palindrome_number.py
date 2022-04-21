# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False

        # split x into two parts, lhs and rhs.
        lhs, rhs = x, 0
        while lhs > rhs:
            hi, lo = lhs // 10, lhs % 10
            lhs, rhs = hi, rhs * 10 + lo

        if lhs == rhs:
            return True
        else:
            return lhs == rhs // 10
