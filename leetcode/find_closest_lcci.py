# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        distance = len(words)
        pos1, pos2 = -1, -1
        for i, word in enumerate(words):
            if word == word1:
                pos1 = i
            if word == word2:
                pos2 = i
            if pos1 >= 0 and pos2 >= 0:
                distance = min(distance, abs(pos1 - pos2))
        return distance
