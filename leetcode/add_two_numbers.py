# -*- coding: utf-8 -*-

from leetcode.utils.singly_linked_list import ListNode, build, dump # noqa


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


def print_node(node: ListNode) -> None:
    r = dump(node)
    print(' -> '.join([str(n) for n in r]))


if __name__ == '__main__':

    i1, i2 = [2, 4, 3], [5, 6, 4]
    l1, l2 = build(i1), build(i2)
    print_node(l1)
    print_node(l2)
    s = Solution()
    r = s.addTwoNumbers(l1, l2)
    print_node(r)
