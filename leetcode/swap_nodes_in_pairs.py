# -*- coding: utf-8 -*-
from leetcode.utils.singly_linked_list import ListNode, build, dump


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


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(f' Input: {nums}')
    head = build(nums)
    s = Solution()
    x = s.swapPairs(head)
    r = dump(x)
    print(f' Output: {r}')
