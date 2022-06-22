# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        outputs = [intervals[0]]
        for i in range(1, len(intervals)):
            last_interval = outputs[-1]
            curr_left, curr_right = intervals[i]
            if last_interval[1] < curr_left:
                outputs.append(intervals[i])
            else:
                last_interval[1] = max(last_interval[1], curr_right)

        return outputs
