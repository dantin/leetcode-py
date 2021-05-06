# -*- coding: utf-8 -*-
import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int) -> None:
            nonlocal path
            if rest == 0:
                res.append(path[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                path.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            path = path[:-most]

        freq = sorted(collections.Counter(candidates).items())
        res = []
        path = []
        dfs(0, target)
        return res
