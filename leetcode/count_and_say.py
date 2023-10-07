# -*- coding: utf-8 -*-

class Solution:
    def countAndSay(self, n: int) -> str:
        preval, retval = '', '1'

        for _ in range(1, n):
            preval, retval = retval, ''

            slow, fast = 0, 0
            while fast < len(preval):
                while fast < len(preval) and preval[fast] == preval[slow]:
                    fast += 1
                retval += f'{fast - slow}{preval[slow]}'
                slow = fast

        return retval
