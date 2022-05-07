# -*- coding: utf-8 -*-
from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0

        bank = set(bank)
        if end not in bank:
            return -1
        q = deque([(start, 0)])
        while q:
            gene, step = q.popleft()
            for i, x in enumerate(gene):
                for y in 'ACGT':
                    mutate = gene[:i] + y + gene[i + 1:]
                    if mutate in bank:
                        if mutate == end:
                            return step + 1
                        bank.remove(mutate)
                        q.append((mutate, step + 1))
        return -1
