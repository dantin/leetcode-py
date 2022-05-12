# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minDeleteionSize(self, strs: List[str]) -> int:
        count = 0
        for column in zip(*strs):
            s0, s1 = ''.join(column), ''.join(sorted(column))
            if s0 != s1:
                count += 1

        return count
