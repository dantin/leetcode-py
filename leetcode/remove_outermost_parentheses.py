# -*- coding: utf-8 -*-

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ''
        stack = []
        for c in s:
            if c == ')':
                stack.pop()
            if stack:
                ans += c
            if c == '(':
                stack.append(c)
        return ans
