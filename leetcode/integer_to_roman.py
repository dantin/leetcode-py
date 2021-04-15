# -*- coding: utf-8 -*-

_ROMAN_DIGITS = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
    (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_digits = []
        for val, symbol in _ROMAN_DIGITS:
            if num == 0:
                break
            count, num = divmod(num, val)
            roman_digits.append(symbol * count)
        return ''.join(roman_digits)
