# -*- coding: utf-8 -*-
from typing import List
from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # add index to original intervals.
        sections = [[*interval, i] for i, interval in enumerate(intervals)]
        sections.sort()

        n = len(sections)
        result = [-1] * n
        for _, end, idx in sections:
            # here '[end]' is a must, as each element in sections is a list.
            i = bisect_left(sections, [end])
            if i < n:
                result[idx] = sections[i][2]
        return result
