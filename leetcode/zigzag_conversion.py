# -*- coding: utf-8 -*-

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        res = ['' for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag

        return ''.join(res)


if __name__ == '__main__':
    orig, row = 'PAYPALISHIRING', 3
    print(f' Input: s = "{orig}", numRows = {row}')
    s = Solution()
    o = s.convert(orig, row)
    print(f' Output: "{o}"')
