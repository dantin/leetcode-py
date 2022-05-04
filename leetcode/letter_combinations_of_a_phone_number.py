# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        if not digits:
            return combinations

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        cache = []

        def backtrace(idx: int):
            if idx == len(digits):
                combinations.append(''.join(cache))
            else:
                digit = digits[idx]
                for letter in phone_map[digit]:
                    cache.append(letter)
                    backtrace(idx + 1)
                    cache.pop()

        backtrace(0)
        return combinations
