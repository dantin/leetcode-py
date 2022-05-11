# -*- coding: utf-8 -*-
from .utils.binary_search_tree import TreeNode


class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return ''

        def dfs(root):
            if not root:
                return
            data.append(root.val)
            dfs(root.left)
            dfs(root.right)

        data = []
        dfs(root)

        return ','.join(str(x) for x in data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        def dfs(left, right):
            if left > right:
                return None

            val = int(ss[left])

            i = left + 1
            while i <= right and int(ss[i]) <= val:
                i += 1

            node = TreeNode(val)
            node.left = dfs(left + 1, i - 1)
            node.right = dfs(i, right)
            return node

        ss = data.split(',')
        return dfs(0, len(ss) - 1)
