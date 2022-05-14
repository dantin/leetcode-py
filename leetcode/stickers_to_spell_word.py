# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        def dfs(state: int) -> int:
            if memo[state] != -1:
                return memo[state]

            ans = t_len + 1
            for sticker in stickers:
                cnt = [0] * 26
                for ch in sticker:
                    cn = ord(ch) - ord('a')
                    cnt[cn] += 1

                nstate = state
                for i, ch in enumerate(target):
                    cn = ord(ch) - ord('a')
                    if (nstate >> i) & 1 and cnt[cn] > 0:
                        cnt[cn] -= 1
                        nstate ^= (1 << i)

                if nstate < state:
                    ans = min(ans, dfs(nstate) + 1)

            memo[state] = ans
            return ans

        t_len = len(target)
        memo = [-1] * (1 << t_len)
        memo[0] = 0

        count = dfs((1 << t_len) - 1)

        return count if count <= t_len else -1
