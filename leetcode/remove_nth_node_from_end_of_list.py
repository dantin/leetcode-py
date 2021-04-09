# -*- coding: utf-8 -*-
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first, second = head, dummy

        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next


def build_list(nums: List[int]) -> ListNode:
    dummy = ListNode()
    tail = dummy
    for n in nums:
        node = ListNode(n)
        tail.next = node
        tail = node
    return dummy.next


def encode_list(head: ListNode) -> List[int]:
    res = []
    while head is not None:
        res.append(head.val)
        head = head.next
    return res


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    n = 2
    print(f' Input head = {head}, n = {n}')
    head = build_list(head)
    s = Solution()
    node = s.removeNthFromEnd(head, n)
    nums = encode_list(node)
    print(f' Output: {nums}')
