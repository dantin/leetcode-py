# -*- coding: utf-8 -*-
from collections import deque
from typing import List, Optional

from .utils.binary_search_tree import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        output = []
        q = deque()
        q.append((root, 0))
        while q:
            node, level = q.popleft()
            if level + 1 > len(output):
                output.append(node.val)
            output[level] = max(node.val, output[level])
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return output
