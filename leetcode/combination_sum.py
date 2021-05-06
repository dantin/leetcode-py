# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates: List[int],
                begin: int, size: int,
                path: List[int],
                res: List[List[int]],
                target: int) -> None:
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return

            for idx in range(begin, size):
                elem = candidates[idx]
                dfs(candidates, idx, size, path + [elem], res, target - elem)

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res
