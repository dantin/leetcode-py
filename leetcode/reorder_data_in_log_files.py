# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_func(s: str) -> tuple:
            lhs, rhs = s.split(' ', 1)
            return (0, rhs, lhs) if rhs[0].isalpha() else (1,)

        logs.sort(key=sort_func)
        return logs
