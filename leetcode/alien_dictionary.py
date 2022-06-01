# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        g = {}
        for c in words[0]:
            g[c] = []
        for i in range(0, len(words) - 1):
            s, t = words[i], words[i + 1]
            for c in t:
                g.setdefault(c, [])
            for u, v in zip(s, t):
                if u != v:
                    g[u].append(v)
                    break
            else:
                if len(s) > len(t):
                    return ""

        visiting, visited = 1, 2
        states = {}
        order = []

        def dfs(u: str) -> bool:
            states[u] = visiting
            for v in g[u]:
                if v not in states:
                    if not dfs(v):
                        return False
                elif states[v] == visiting:
                    return False
            order.append(u)
            states[u] = visited
            return True

        return ''.join(reversed(order)) if all(dfs(u) for u in g if u not in states) else ''
