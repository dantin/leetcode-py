# -*- coding: utf-8 -*-
class Node:
    def __init__(self, left=None, right=None, val=0, lazy=0):
        """
        left: left child
        right: right child
        val: value
        lazy: lazy flag
        """
        self.left = left
        self.right = right
        self.val = val
        self.lazy = lazy


class SegmentTree:
    def __init__(self, size):
        """
        size: size of segment tree.
        """
        self.size = size
        self.root = Node()

    def push_down(self, node, start, end):
        """
        update downward, forward lazy flag.

        node: current node
        start: left boundary of current node
        end: right boundary of current node
        """
        mid = start + ((end - start) >> 1)
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy == 0:
            return
        node.left.val += node.lazy * (mid - start + 1)
        node.right.val += node.lazy * (end - mid)
        node.left.lazy += node.lazy
        node.right.lazy += node.lazy
        node.lazy = 0

    def push_up(self, node):
        """
        update upward, all child node should be updated.

        node: current node
        """
        node.val = node.left.val + node.right.val

    def update(self, node, start, end, left, right, add):
        """
        update section `[left, right]`, put add tag to each value in this section;
        the intersection between `[left, right]` and current node managed `[start, end]` should not
        be empty.

        node: current node
        start: left boundry of current node
        end: right boundry of current node
        left: left boundry of changed section
        right: right boundry of changed section
        add: addition
        """
        if left <= start and end <= right:
            node.val += add * (end - start + 1)
            node.lazy += add
            return

        self.push_down(node, start, end)
        mid = start + ((end - start) >> 1)

        if left <= mid:
            self.update(node.left, start, mid, left, right, add)
        if right > mid:
            self.update(node.right, mid + 1, end, left, right, add)

        self.push_up(node)

    def query(self, node, start, end, left, right):
        """
        query in section `[left, right]`
        the intersection between `[left, right]` and current node managed `[start, end]` should not
        be empty.

        node: current node
        start: left boundry of current node
        end: right boundry of current node
        left: left boundry of changed section
        right: right boundry of changed section
        add: addition
        """
        if left <= start and end <= right:
            return node.val

        self.push_down(node, start, end)

        mid = start + ((end - start) >> 1)
        out = 0
        if left <= mid:
            out += self.query(node.left, start, mid, left, right)
        if right > mid:
            out += self.query(node.right, mid + 1, end, left, right)

        return out


class MyCalendar:
    def __init__(self):
        size = 10 ** 9
        self.size = size
        self.tree = SegmentTree(size)

    def book(self, start: int, end: int) -> bool:
        if self.tree.query(self.tree.root, 0, self.size, start, end - 1) != 0:
            return False
        self.tree.update(self.tree.root, 0, self.size, start, end - 1, 1)
        return True
