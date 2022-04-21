# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        mid = (len1 + len2) // 2
        if (len1 + len2) % 2 == 1:
            return float(find_kth(nums1, nums2, mid + 1))
        else:
            lhs = find_kth(nums1, nums2, mid)
            rhs = find_kth(nums1, nums2, mid + 1)
            return (lhs + rhs) / 2.0


def find_kth(nums1: List[int], nums2: List[int], k: int) -> int:
    """find kth element in num1 and num2, k is index start from 1."""
    len1, len2 = len(nums1), len(nums2)
    # make sure that nums1 is always the smaller one.
    if len1 > len2:
        return find_kth(nums2, nums1, k)

    if len1 == 0:  # num1 is empty
        return nums2[k - 1]

    if k == 1:
        return min(nums1[0], nums2[0])

    # devide k into two parts.
    i1 = min(k // 2, len1)
    i2 = k - i1
    if nums1[i1 - 1] < nums2[i2 - 1]:
        return find_kth(nums1[i1:], nums2[:], k - i1)
    elif nums1[i1 - 1] > nums2[i2 - 1]:
        return find_kth(nums1[:], nums2[i2:], k - i2)
    else:
        return nums1[i1 - 1]
