# -*- coding: utf-8 -*-
from typing import Optional

from .utils.binary_search_tree import TreeNode


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            node = root.right
            while node.left:
                node = node.left
            node.right = self.deleteNode(root.right, node.val)
            node.left = root.left
            return node

        return root
