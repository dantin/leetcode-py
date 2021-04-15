# -*- coding: utf-8 -*-

from leetcode.utils.singly_linked_list import ListNode


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
