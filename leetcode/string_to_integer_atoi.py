# -*- coding: utf-8 -*-

class Solution:
    def myAtoi(self, s: str) -> int:
        return s


if __name__ == '__main__':
    x = '42'
    print(f' Input: s = {x}')
    s = Solution()
    y = s.myAtoi(x)
    print(f' Output: {y}')
