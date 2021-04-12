# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrace(s, left, right):
            if len(s) == 2 * n:
                ans.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backtrace(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrace(s, left, right + 1)
                s.pop()

        backtrace([], 0, 0)
        return ans


if __name__ == '__main__':
    n = 3
    print(f' Input: n = {n}')
    s = Solution()
    x = s.generateParenthesis(n)
    print(f' Output: {x}')
