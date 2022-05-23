# -*- coding: utf-8 -*-
from collections import deque
from typing import List


_DIRS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m = len(forest)
        n = len(forest[0])
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        pre_x, pre_y = 0, 0
        total = 0
        for height, cur_x, cur_y in trees:
            steps = bfs(forest, pre_x, pre_y, cur_x, cur_y)
            if steps == -1:
                return -1
            total += steps
            pre_x, pre_y = cur_x, cur_y
        return total


def bfs(forest, start_x, start_y, target_x, target_y):
    m = len(forest)
    n = len(forest[0])
    steps = 0
    queue = deque()
    queue.append((start_x, start_y))
    visited = set()
    visited.add((start_x, start_y))
    while queue:
        size = len(queue)
        for _ in range(size):
            cur_x, cur_y = queue.popleft()
            if cur_x == target_x and cur_y == target_y:
                return steps
            for delta_x, delta_y in _DIRS:
                new_x = cur_x + delta_x
                new_y = cur_y + delta_y
                if (0 <= new_x < m and
                        0 <= new_y < n and
                        forest[new_x][new_y] != 0 and
                        ((new_x, new_y) not in visited)):
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))
        steps += 1
    return -1
