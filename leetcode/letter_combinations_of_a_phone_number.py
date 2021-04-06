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
        combination = []

        def backtrace(idx: int):
            if idx == len(digits):
                combinations.append(''.join(combination))
            else:
                digit = digits[idx]
                for letter in phone_map[digit]:
                    combination.append(letter)
                    backtrace(idx + 1)
                    combination.pop()

        backtrace(0)
        return combinations


if __name__ == '__main__':
    digits = '23'
    print(f' Input: digits = {digits}')
    s = Solution()
    r = s.letterCombinations(digits)
    print(f' Output: {r}')
