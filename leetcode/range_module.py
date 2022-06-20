# -*- coding: utf-8 -*-

MAX_VAL = int(1e9 + 7)


class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.val = False
        self.add = False


class SegmentTree:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def update(node: Node, low: int, hi: int, left: int, right: int, v: bool) -> None:
        if left <= low and hi <= right:
            node.val = v
            node.add = True
            return

        SegmentTree.pushdown(node)
        mid = (low + hi) >> 1
        if left <= mid:
            SegmentTree.update(node.left, low, mid, left, right, v)
        if right > mid:
            SegmentTree.update(node.right, mid + 1, hi, left, right, v)
        SegmentTree.pushup(node)

    @staticmethod
    def query(node: Node, low: int, hi: int, left: int, right: int) -> bool:
        if left <= low and hi <= right:
            return node.val

        SegmentTree.pushdown(node)
        mid, ans = (low + hi) >> 1, True
        if left <= mid:
            ans = ans and SegmentTree.query(node.left, low, mid, left, right)
        if right > mid:
            ans = ans and SegmentTree.query(node.right, mid + 1, hi, left, right)
        return ans

    @staticmethod
    def pushdown(node: Node) -> None:
        if not node.left:
            node.left = Node()
        if not node.right:
            node.right = Node()
        if not node.add:
            return
        node.left.val, node.right.val = node.val, node.val
        node.left.add, node.right.add = True, True
        node.add = False

    @staticmethod
    def pushup(node: Node) -> None:
        node.val = node.left.val and node.right.val


class RangeModule:
    def __init__(self):
        self.segment_tree = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        SegmentTree.update(self.segment_tree.root, 1, MAX_VAL, left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return SegmentTree.query(self.segment_tree.root, 1, MAX_VAL, left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        SegmentTree.update(self.segment_tree.root, 1, MAX_VAL, left, right - 1, False)
