# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def backtrack(n: int, k: int, pos: int, buff: List[int]) -> None:
            if pos == n:
                return
            cnt = fractorial[n - 1 - pos]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                buff.append(i)
                used[i] = True
                backtrack(n, k, pos + 1, buff)
                return

        if n == 0:
            return ''

        fractorial = [1] * (n + 1)
        for i in range(2, n + 1):
            fractorial[i] = fractorial[i - 1] * i

        used = [False] * (n + 1)
        buff = []

        backtrack(n, k, 0, buff)
        return ''.join(str(n) for n in buff)
