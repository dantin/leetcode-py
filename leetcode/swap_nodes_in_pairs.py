# -*- coding: utf-8 -*-
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        tail = dummy
        while tail.next and tail.next.next:
            n1 = tail.next
            n2 = tail.next.next
            tail.next = n2
            n1.next = n2.next
            n2.next = n1
            tail = n1
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
    nums = [1, 2, 3, 4]
    print(f' Input: {nums}')
    head = make_list(nums)
    r = dump_list(head)
    s = Solution()
    x = s.swapPairs(head)
    r = dump_list(x)
    print(f' Output: {r}')
