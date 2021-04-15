# -*- coding: utf-8 -*-
"""Common definition and func of singly-linked list."""

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build(nums: List[int]) -> ListNode:
    dummy = ListNode()
    tail = dummy
    for n in nums:
        tail.next = ListNode(val=n)
        tail = tail.next
    return dummy.next


def dump(head: ListNode) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
