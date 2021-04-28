# -*- coding: utf-8 -*-

class Solution:
    def countAndSay(self, n: int) -> str:
        pre, cur = '', '1'
        for _ in range(1, n):
            pre, cur = cur, ''
            fast, slow = 0, 0
            while fast < len(pre):
                while fast < len(pre) and pre[fast] == pre[slow]:
                    fast += 1
                cur += f'{fast - slow}{pre[slow]}'
                slow = fast
        return cur
