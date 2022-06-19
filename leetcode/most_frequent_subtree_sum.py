# -*- coding: utf-8 -*-
from collections import Counter
from typing import List

from leetcode.utils.binary_search_tree import TreeNode


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = Counter()

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            cnt[total] += 1
            return total

        dfs(root)
        max_cnt = max(cnt.values())
        return [t for t, c in cnt.items() if c == max_cnt]
