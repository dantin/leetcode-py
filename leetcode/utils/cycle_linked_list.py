# -*- coding: utf-8 -*-
"""Common definition and func of cycle linked list."""

from typing import List


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(nums: List[int]) -> Node:
    dummy = Node()
    tail = dummy
    for n in nums:
        tail.next = Node(val=n)
        tail = tail.next
    tail.next = dummy.next
    return dummy.next


def dump(head: Node) -> List[int]:
    if not head:
        return []
    res = [head.val]
    ptr = head.next
    while ptr != head:
        res.append(ptr.val)
        ptr = ptr.next
    return res
