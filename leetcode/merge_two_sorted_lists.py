# -*- coding: utf-8 -*-

from leetcode.utils.singly_linked_list import ListNode, build, dump


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


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 4], [1, 3, 4]
    print(f' Input: l1 = {nums1}, l2 = {nums2}')
    l1, l2 = build(nums1), build(nums2)
    s = Solution()
    x = s.mergeTwoLists(l1, l2)
    res = dump(x)
    print(f' Output: {res}')
