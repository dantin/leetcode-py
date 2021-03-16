# -*- coding: utf-8 -*-
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = 0
        dummy = ListNode()
        tail = dummy
        while l1 or l2:
            if l1:
                val += l1.val
            if l2:
                val += l2.val
            tail.next = ListNode(val % 10)
            val = val // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            tail = tail.next

        while val > 0:
            tail.next = ListNode(val % 10)
            val = val // 10
            tail = tail.next
        return dummy.next


def make_node(n: List[int]) -> ListNode:
    dummy = ListNode()
    tail = dummy
    for i in n:
        tail.next = ListNode(i)
        tail = tail.next
    return dummy.next


def print_node(node: ListNode) -> None:
    while node:
        print(node.val, end='')
        if node.next:
            print(' -> ', end='')
        node = node.next
    print()


if __name__ == '__main__':
    i1 = [2, 4, 3]
    i2 = [5, 6, 4]
    l1 = make_node(i1)
    l2 = make_node(i2)
    print_node(l1)
    print_node(l2)
    s = Solution()
    r = s.addTwoNumbers(l1, l2)
    print_node(r)
