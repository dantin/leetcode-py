# -*- coding: utf-8 -*-
from collections import deque
from typing import Optional

from .utils.binary_search_tree import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        output = 0

        q = deque([root])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            output = node.val

        return output
