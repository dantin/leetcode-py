# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        lhs, rhs = x, 0
        while lhs > rhs:
            hi, lo = lhs // 10, lhs % 10
            lhs, rhs = hi, rhs * 10 + lo
        print(lhs, rhs)
        if lhs == rhs:
            return True
        else:
            return lhs == rhs // 10


if __name__ == '__main__':
    x = 121
    print(f' Input: x = {x}')
    s = Solution()
    y = s.isPalindrome(x)
    print(f' Output: {y}')
