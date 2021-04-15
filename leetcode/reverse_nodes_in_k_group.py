# -*- coding: utf-8 -*-
from typing import Tuple

from leetcode.utils.singly_linked_list import build, dump, ListNode


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


if __name__ == '__main__':
    nums, k = [1, 2, 3, 4, 5], 2
    print(f' Input: head = {nums}, k = {k}')
    head = build(nums)
    s = Solution()
    x = s.reverseKGroup(head, k)
    r = dump(x)
    print(f' Output: {r}')
