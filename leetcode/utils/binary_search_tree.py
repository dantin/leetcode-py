# -*- coding: utf-8 -*-
from typing import List


class TreeNode:
    """Definition of a Binary Tree Node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree(nums: List[int], pos: int) -> TreeNode:
    if nums[pos] is None:
        return None

    left, right = 2 * pos + 1, 2 * pos + 2

    node = TreeNode(nums[pos])
    if left < len(nums):
        node.left = make_tree(nums, left)
    if right < len(nums):
        node.right = make_tree(nums, right)

    return node


def find_node(root: TreeNode, val: int) -> TreeNode:
    nodes = []
    current = root
    while nodes or current:
        while current:
            nodes.append(current)
            current = current.left
        current = nodes.pop()
        if current.val == val:
            return current
        current = current.right
    return None
