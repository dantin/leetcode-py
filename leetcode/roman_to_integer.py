# -*- coding: utf-8 -*-

_ROMAN_DIGITS = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}


class Solution:
    def romanToInt(self, s: str) -> int:
        n, i = 0, 0
        while i < len(s):
            if s[i:i + 2] in _ROMAN_DIGITS:
                n += _ROMAN_DIGITS[s[i:i + 2]]
                i += 2
            else:
                n += _ROMAN_DIGITS[s[i:i + 1]]
                i += 1
        return n
