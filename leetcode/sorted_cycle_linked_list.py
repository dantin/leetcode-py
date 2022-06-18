# -*- coding: utf-8 -*-
from leetcode.utils.cycle_linked_list import Node


class Solution:
    def insert(self, head: Node, val: int) -> Node:
        if head is None:
            node = Node(val)
            node.next = node
            return node

        ptr = head
        while ptr.next != head:
            if ptr.val <= val <= ptr.next.val:
                break
            if ptr.val > ptr.next.val and (val <= ptr.next.val or val >= ptr.val):
                break
            ptr = ptr.next
        ptr.next = Node(val, ptr.next)
        return head
