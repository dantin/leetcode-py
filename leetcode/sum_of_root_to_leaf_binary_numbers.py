# -*- coding: utf-8 -*-
from collections import deque
from typing import Optional

from .utils.binary_search_tree import TreeNode


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 0))
        total = 0
        while queue:
            node, n = queue.popleft()
            val = 2 * n + node.val
            if node.left:
                queue.append((node.left, val))
            if node.right:
                queue.append((node.right, val))

            if not node.left and not node.right:
                total += val

        return total
