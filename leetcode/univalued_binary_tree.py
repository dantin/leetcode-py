# -*- coding: utf-8 -*-
from collections import deque

from .utils.binary_search_tree import TreeNode


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        value = root.val
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val != value:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True
