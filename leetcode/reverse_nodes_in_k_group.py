# -*- coding: utf-8 -*-
from typing import List, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse_list(head: ListNode, tail: ListNode) -> Tuple[ListNode, ListNode]:
            pre = tail.next
            p = head
            while pre != tail:
                tmp = p.next
                p.next = pre
                pre = p
                p = tmp
            return tail, head

        dummy = ListNode()
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            tmp = tail.next
            head, tail = reverse_list(head, tail)
            pre.next = head
            tail.next = tmp
            pre = tail
            head = tail.next

        return dummy.next


def make_list(nums: List[int]) -> ListNode:
    dummy = ListNode()
    tail = dummy
    for n in nums:
        tail.next = ListNode(val=n)
        tail = tail.next
    return dummy.next


def dump_list(head: ListNode) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == '__main__':
    nums, k = [1, 2, 3, 4, 5], 2
    print(f' Input: head = {nums}, k = {k}')
    head = make_list(nums)
    s = Solution()
    x = s.reverseKGroup(head, k)
    r = dump_list(x)
    print(f' Output: {r}')
