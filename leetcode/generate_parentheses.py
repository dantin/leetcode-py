# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cache = []

        def backtrace(buffer, left, right):
            if len(buffer) == 2 * n:
                cache.append(''.join(buffer))
                return
            if left < n:
                buffer.append('(')
                backtrace(buffer, left + 1, right)
                buffer.pop()
            if right < left:
                buffer.append(')')
                backtrace(buffer, left, right + 1)
                buffer.pop()

        backtrace([], 0, 0)
        return cache
