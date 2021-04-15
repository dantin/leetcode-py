# -*- coding: utf-8 -*-
from typing import List

from leetcode.utils.singly_linked_list import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode()
        tail = dummy
        cache = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(cache, (head.val, i))
                lists[i] = lists[i].next
        while cache:
            val, i = heapq.heappop(cache)
            tail.next = ListNode(val)
            tail = tail.next
            if lists[i]:
                heapq.heappush(cache, (lists[i].val, i))
                lists[i] = lists[i].next
        return dummy.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        def merge_list(l1: ListNode, l2: ListNode) -> ListNode:
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

        def merge(lists: List[ListNode], left: int, right: int) -> ListNode:
            if left == right:
                return lists[left]
            mid = left + (right - left) // 2
            l1 = merge(lists, left, mid)
            l2 = merge(lists, mid + 1, right)
            return merge_list(l1, l2)
        n = len(lists)
        return merge(lists, 0, n - 1)
