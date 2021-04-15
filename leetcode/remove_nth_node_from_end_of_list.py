# -*- coding: utf-8 -*-
from leetcode.utils.singly_linked_list import ListNode, build, dump


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


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    n = 2
    print(f' Input head = {head}, n = {n}')
    head = build(head)
    s = Solution()
    node = s.removeNthFromEnd(head, n)
    nums = dump(node)
    print(f' Output: {nums}')
