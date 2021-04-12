# -*- coding: utf-8 -*-
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next


def make_list(nums: List[int]) -> ListNode:
    dummy = ListNode()
    tail = dummy
    for n in nums:
        node = ListNode(val=n)
        tail.next = node
        tail = node
    return dummy.next


def dump_list(head: ListNode) -> List[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 4], [1, 3, 4]
    print(f' Input: l1 = {nums1}, l2 = {nums2}')
    l1, l2 = make_list(nums1), make_list(nums2)
    s = Solution()
    x = s.mergeTwoLists(l1, l2)
    res = dump_list(x)
    print(f' Output: {res}')
