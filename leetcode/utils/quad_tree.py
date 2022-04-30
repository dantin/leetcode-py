# -*- coding: utf-8 -*-
from typing import Any, List


class Node:
    """Definition for a QuadTree node."""
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


def dump(root: Node) -> List[Any]:
    res = []
    q = []
    q.append(root)
    while q:
        node = q.pop(0)
        if not node:
            res.append('null')
            continue
        q.append(node.topLeft)
        q.append(node.topRight)
        q.append(node.bottomLeft)
        q.append(node.bottomRight)
        res.append([int(node.isLeaf), int(node.val)])
    i = len(res) - 1
    while i >= 0:
        if res[i] != 'null':
            break
        i -= 1
    return res[:i + 1]
