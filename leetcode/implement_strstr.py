# -*- coding: utf-8 -*-
from typing import Dict


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def init_shift_mat(s: str) -> Dict[str, int]:
            mat = {}
            for i in range(len(s) - 1, -1, -1):
                if s[i] not in mat:
                    mat[s[i]] = len(s) - i
            mat['ot'] = len(s) + 1
            return mat

        if len(needle) > len(haystack):
            return -1
        if not needle:
            return 0

        mat = init_shift_mat(needle)
        i = 0
        while i + len(needle) <= len(haystack):
            target = haystack[i:i + len(needle)]
            if target == needle:
                return i
            else:
                if i + len(needle) >= len(haystack):
                    return -1
                cur_c = haystack[i + len(needle)]
                if cur_c in mat:
                    i += mat[cur_c]
                else:
                    i += mat['ot']
        return -1 if i + len(needle) >= len(haystack) else i
