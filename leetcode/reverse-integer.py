# -*- coding: utf-8 -*-

class Solution:
    def reverse(self, x: int) -> int:
        is_neg = True if x < 0 else False
        if x < 0:
            x = -x

        limit = 2 ** 31
        n = 0
        while x > 0:
            n = n * 10
            n += x % 10
            x //= 10
        if is_neg:
            return 0 if n > limit else -n
        else:
            return 0 if n >= limit else n


if __name__ == '__main__':
    x = 123
    print(f' Input: x = {x}')
    s = Solution()
    y = s.reverse(x)
    print(f' Output: {y}')
