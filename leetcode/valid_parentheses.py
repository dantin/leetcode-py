# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


if __name__ == '__main__':
    x = '()'
    print(f' Input: s = "{x}"')
    s = Solution()
    r = s.isValid(x)
    print(f' Output: {r}')
