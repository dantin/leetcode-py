# -*- coding: utf-8 -*-

class Solution:
    def myAtoi(self, s: str) -> int:
        start, n = 0, 0
        for c in s:
            if c == ' ':
                start += 1
            else:
                break

        if start == len(s):
            return n
        is_neg = True if s[start] == '-' else False
        if s[start] in ('+', '-'):
            start += 1

        for c in s[start:]:
            if str.isdigit(c):
                n *= 10
                n += int(c)
            else:
                break

        limit = 2 ** 31
        if is_neg:
            return -n if n < limit else -limit
        else:
            return n if n < limit else limit - 1


if __name__ == '__main__':
    x = '42'
    print(f' Input: s = {x}')
    s = Solution()
    y = s.myAtoi(x)
    print(f' Output: {y}')
