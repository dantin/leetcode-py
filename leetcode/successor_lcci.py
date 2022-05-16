# -*- coding: utf-8 -*-
from .utils.binary_search_tree import TreeNode


class Solution:
    def inorderSucessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        nodes = []
        previous, current = None, root
        while nodes or current:
            while current:
                nodes.append(current)
                current = current.left
            current = nodes.pop()
            if previous == p:
                return current
            previous = current
            current = current.right
        return None
