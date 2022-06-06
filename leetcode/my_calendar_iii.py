# -*- coding: utf-8 -*-
class Node:
    def __init__(self, lo, hi):
        self.left = None
        self.right = None
        self.lo = lo
        self.hi = hi
        self.mid = (lo + hi) // 2
        self.val = 0
        self.add = 0


class SegmentTree:
    def __init__(self):
        self.root = Node(1, int(1e9 + 1))

    def modify(self, lo, hi, val, node=None):
        if lo > hi:
            return
        if not node:
            node = self.root
        if node.lo >= lo and node.hi <= hi:
            node.val += val
            node.add += val
            return
        self.pushdown(node)
        if lo <= node.mid:
            self.modify(lo, hi, val, node.left)
        if hi > node.mid:
            self.modify(lo, hi, val, node.right)
        self.pushup(node)

    def query(self, lo, hi, node=None):
        if lo > hi:
            return 0
        if not node:
            node = self.root
        if node.lo >= lo and node.hi <= hi:
            return node.val
        self.pushdown(node)
        val = 0
        if lo <= node.mid:
            val = max(val, self.query(lo, hi, node.left))
        if hi > node.mid:
            val = max(val, self.query(lo, hi, node.right))
        return val

    def pushup(self, node):
        node.val = max(node.left.val, node.right.val)

    def pushdown(self, node):
        if not node.left:
            node.left = Node(node.lo, node.mid)
        if not node.right:
            node.right = Node(node.mid + 1, node.hi)
        if node.add:
            node.left.val += node.add
            node.right.val += node.add
            node.left.add += node.add
            node.right.add += node.add
            node.add = 0


class MyCalendarThree:
    def __init__(self):
        self.tree = SegmentTree()

    def book(self, start: int, end: int) -> int:
        self.tree.modify(start + 1, end, 1)
        return self.tree.query(1, int(1e9 + 1))
