# -*- coding: utf-8 -*-

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if m < n:
            return self.oneEditAway(second, first)

        if m - n > 1:
            return False

        for i, (lhs, rhs) in enumerate(zip(first, second)):
            if lhs != rhs:
                if m == n:
                    first[i + 1:] == second[i + 1:]
                else:
                    first[i + 1:] == second[i:]
        return True
