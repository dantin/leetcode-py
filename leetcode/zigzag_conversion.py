# -*- coding: utf-8 -*-

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return ''


if __name__ == '__main__':
    orig, row = 'PAYPALISHIRING', 3
    print(f' Input: s = "{orig}", numRows = {row}')
    s = Solution()
    o = s.convert(orig, row)
    print(f' Output: "{o}"')
