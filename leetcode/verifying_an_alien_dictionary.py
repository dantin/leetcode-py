# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {ch: i for i, ch in enumerate(order)}

        original = []
        for s in words:
            text = ''.join(chr(ord('a') + index[ch]) for ch in s)
            original.append(text)
        return original == sorted(original)
