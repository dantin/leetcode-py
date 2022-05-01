# -*- coding: utf-8 -*-
from typing import List

from .utils.binary_search_tree import TreeNode


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode, trace: List[int]) -> None:
            if node:
                inorder(node.left, trace)
                trace.append(node.val)
                inorder(node.right, trace)

        nums1, nums2 = [], []
        inorder(root1, nums1)
        inorder(root2, nums2)

        merged = []
        lhs, s1 = 0, len(nums1)
        rhs, s2 = 0, len(nums2)
        while True:
            if lhs == s1:
                merged.extend(nums2[rhs:])
                break
            if rhs == s2:
                merged.extend(nums1[lhs:])
                break

            if nums1[lhs] < nums2[rhs]:
                merged.append(nums1[lhs])
                lhs += 1
            else:
                merged.append(nums2[rhs])
                rhs += 1

        return merged
