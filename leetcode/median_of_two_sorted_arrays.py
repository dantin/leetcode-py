# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return float(find_kth(nums1, 0, len1, nums2, 0, len2, (len1 + len2 + 1) // 2))
        else:
            mid = (len1 + len2) // 2
            lhs = find_kth(nums1, 0, len(nums1), nums2, 0, len(nums2), mid)
            rhs = find_kth(nums1, 0, len(nums1), nums2, 0, len(nums2), mid + 1)
            return (lhs + rhs) / 2.0


def find_kth(
    nums1: List[int], begin1: int, end1: int,
    nums2: List[int], begin2: int, end2: int,
    k: int,
) -> int:
    """find kth element in num1 and num2, k is index start from 1."""
    n = end1 - begin1
    m = end2 - begin2

    if n <= 0:
        return nums2[begin2 + k - 1]
    if m <= 0:
        return nums1[begin1 + k - 1]
    if k == 1:
        return min(nums1[begin1], nums2[begin2])

    # devide k into two parts.
    mid1 = (begin1 + end1) // 2
    mid2 = (begin2 + end2) // 2
    if nums1[mid1] <= nums2[mid2]:
        if (n // 2 + m // 2 + 1) >= k:
            return find_kth(nums1, begin1, end1, nums2, begin2, mid2, k)
        else:
            return find_kth(nums1, mid1 + 1, end1, nums2, begin2, end2, k - n // 2 - 1)
    else:
        if (n // 2 + m // 2 + 1) >= k:
            return find_kth(nums1, begin1, mid1, nums2, begin2, end2, k)
        else:
            return find_kth(nums1, begin1, end1, nums2, mid2 + 1, end2, k - m // 2 - 1)
