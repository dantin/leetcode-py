# -*- coding: utf-8 -*-

class Solution:
    def myAtoi(self, s: str) -> int:
        start = 0
        for c in s:
            if c == ' ':
                start += 1
            else:
                break

        n = 0
        if start == len(s):
            return n

        negative = True if s[start] == '-' else False
        if s[start] in ('+', '-'):
            start += 1

        for c in s[start:]:
            if str.isdigit(c):
                n *= 10
                n += int(c)
            else:
                break

        limit = 2 ** 31
        if negative:
            return -n if n < limit else -limit
        else:
            return n if n < limit else limit - 1
