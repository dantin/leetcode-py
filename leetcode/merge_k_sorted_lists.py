# -*- coding: utf-8 -*-
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(f' Input: lists = {lists}')
    s = Solution()
    x = []
    for nums in lists:
        head = make_list(nums)
        x.append(head)
    head = s.mergeKLists(x)
    r = dump_list(head)
    print(f' Output: {r}')
