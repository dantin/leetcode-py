# -*- coding: utf-8 -*-
from collections import defaultdict
from random import choice, randrange
from typing import List


class Solution1:
    def __init__(self, nums: List[int]):
        pos = defaultdict(list)
        for i, num in enumerate(nums):
            pos[num].append(i)
        self.pos = pos

    def pick(self, target: int) -> int:
        return choice(self.pos[target])


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        pos = 0
        cnt = 0
        for i, num in enumerate(self.nums):
            if num == target:
                cnt += 1
                if randrange(cnt) == 0:
                    pos = i
        return pos
