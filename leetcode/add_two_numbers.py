# -*- coding: utf-8 -*-
from typing import Optional

from leetcode.utils.singly_linked_list import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
