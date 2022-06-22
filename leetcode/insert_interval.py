# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        outputs = []
        size = len(intervals)
        i = 0
        # no overlap.
        while i < size and intervals[i][1] < newInterval[0]:
            outputs.append(intervals[i])
            i += 1

        # overlap
        while i < size and intervals[i][0] <= newInterval[1]:
            # update left boundary.
            newInterval[0] = min(intervals[i][0], newInterval[0])
            # update right boundary.
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        outputs.append(newInterval)

        # no verlap
        while i < size:
            outputs.append(intervals[i])
            i += 1

        return outputs
