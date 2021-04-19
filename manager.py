# -*- coding: utf-8 -*-

import click


def normalize_token(token_name: str) -> str:
    return token_name.replace('_', '-')


@click.group(
    context_settings={'token_normalize_func': normalize_token},
)
def cli() -> None:
    """This is a management script for running leetcode solution in the console."""
    pass


@cli.command()
def two_sum() -> None:
    """1# Two Sum."""
    from leetcode.two_sum import Solution

    nums, target = [2, 7, 11, 15], 9

    print(f'Given nums: {nums}, target = {target}')
    solution = Solution()
    pos = solution.twoSum(nums, target)
    print(f' output: {pos}')


@cli.command()
def add_two_numbers() -> None:
    """2# Add Two Numbers."""
    from leetcode.add_two_numbers import Solution
    from leetcode.utils.singly_linked_list import build, dump, ListNode

    def print_node(node: ListNode) -> None:
        r = dump(node)
        print(' -> '.join([str(n) for n in r]))

    i1, i2 = [2, 4, 3], [5, 6, 4]
    l1, l2 = build(i1), build(i2)
    print_node(l1)
    print_node(l2)
    s = Solution()
    r = s.addTwoNumbers(l1, l2)
    print_node(r)


@cli.command()
def longest_substring_without_repeating_characters() -> None:
    """3# Longest Substring Without Repeating Characters."""
    from leetcode.longest_substring_without_repeating_characters import Solution

    src = "abcabcbb"
    s = Solution()
    print(f'Input s = {src}')
    r = s.lengthOfLongestSubstring(src)
    print(f'Output: {r}')


@cli.command()
def median_of_two_sorted_arrays() -> None:
    """4# Median of Two Sorted Arrays."""
    from leetcode.median_of_two_sorted_arrays import Solution

    nums1, nums2 = [1, 3], [2]
    s = Solution()
    print(f'Input s = {nums1}, nums2 = {nums2}')
    r = s.findMedianSortedArrays(nums1, nums2)
    print(f'Output: {r}')


@cli.command()
def longest_palindromic_substring() -> None:
    """5# Longest Palindromic Substring."""
    from leetcode.longest_palindromic_substring import Solution

    orig = 'badad'
    s = Solution()
    print(f' Input s = {orig}')
    o = s.longestPalindrome(orig)
    print(f' Output: {o}')


@cli.command()
def zigzag_conversion() -> None:
    """6# ZigZag Conversion."""
    from leetcode.zigzag_conversion import Solution

    orig, row = 'PAYPALISHIRING', 3
    print(f' Input: s = "{orig}", numRows = {row}')
    s = Solution()
    o = s.convert(orig, row)
    print(f' Output: "{o}"')


@cli.command()
def reverse_integer() -> None:
    """7# Reverse Integer."""
    from leetcode.reverse_integer import Solution

    x = 123
    print(f' Input: x = {x}')
    s = Solution()
    y = s.reverse(x)
    print(f' Output: {y}')


@cli.command()
def string_to_integer_atoi() -> None:
    """8# String to Integer (atoi)."""
    from leetcode.string_to_integer_atoi import Solution

    x = '42'
    print(f' Input: s = {x}')
    s = Solution()
    y = s.myAtoi(x)
    print(f' Output: {y}')


@cli.command()
def palindrome_number() -> None:
    """9# Palindrome Number."""
    from leetcode.palindrome_number import Solution

    x = 121
    print(f' Input: x = {x}')
    s = Solution()
    y = s.isPalindrome(x)
    print(f' Output: {y}')


@cli.command()
def regular_expression_matching() -> None:
    """10# Regular Expression Matching."""
    from leetcode.regular_expression_matching import Solution

    x, p = 'aa', 'a'
    print(f' Input: s = "{x}", p = "{p}"')
    s = Solution()
    r = s.isMatch(x, p)
    print(f' Output: {r}')


@cli.command()
def container_with_most_water() -> None:
    """11# Container With Most Water."""
    from leetcode.container_with_most_water import Solution

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f' Input: {height}')
    s = Solution()
    r = s.maxArea(height)
    print(f' Output: {r}')


@cli.command()
def integer_to_roman() -> None:
    """12# Integer to Roman."""
    from leetcode.integer_to_roman import Solution

    num = 3
    print(f' Input: num = {num}')
    s = Solution()
    r = s.intToRoman(num)
    print(f' Output: {r}')


@cli.command()
def roman_to_integer() -> None:
    """13# Roman to Integer."""
    from leetcode.roman_to_integer import Solution

    x = 'III'
    print(f' Input: s = {x}')
    s = Solution()
    r = s.romanToInt(x)
    print(f' Output: {r}')


@cli.command()
def longest_common_prefix() -> None:
    """14# Longest Common Prefix."""
    from leetcode.longest_common_prefix import Solution

    strs = ['flower', 'flow', 'flight']
    print(f' Input: strs = {strs}')
    s = Solution()
    r = s.longestCommonPrefix4(strs)
    print(f' Output: {r}')


@cli.command()
def three_sum() -> None:
    """15# 3Sum."""
    from leetcode.three_sum import Solution

    nums = [-1, 0, 1, 2, -1, -4]
    print(f' Input: nums = {nums}')
    s = Solution()
    r = s.threeSum(nums)
    print(f' Output: {r}')


@cli.command()
def three_sum_closest() -> None:
    """16# 3Sum Closest."""
    from leetcode.three_sum_closest import Solution

    nums = [-1, 2, 1, -4]
    target = 1
    print(f' nums = {nums}, target = {target}')
    s = Solution()
    r = s.threeSumClosest(nums, target)
    print(f' Output: {r}')


@cli.command()
def letter_combinations_of_a_phone_number() -> None:
    """17# Letter Combinations of a Phone Number."""
    from leetcode.letter_combinations_of_a_phone_number import Solution

    digits = '23'
    print(f' Input: digits = {digits}')
    s = Solution()
    r = s.letterCombinations(digits)
    print(f' Output: {r}')


@cli.command()
def four_sum() -> None:
    """18# 4Sum."""
    from leetcode.four_sum import Solution

    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(f' Input: nums = {nums}, target = {target}')
    s = Solution()
    r = s.fourSum(nums, target)
    print(f' Output: {r}')


@cli.command()
def remove_nth_node_from_end_of_list() -> None:
    """19# Remove Nth Node From End of List."""
    from leetcode.remove_nth_node_from_end_of_list import Solution
    from leetcode.utils.singly_linked_list import build, dump

    head = [1, 2, 3, 4, 5]
    n = 2
    print(f' Input head = {head}, n = {n}')
    head = build(head)
    s = Solution()
    node = s.removeNthFromEnd(head, n)
    nums = dump(node)
    print(f' Output: {nums}')


@cli.command()
def valid_parentheses() -> None:
    """20# Valid Parentheses."""
    from leetcode.valid_parentheses import Solution

    x = '()'
    print(f' Input: s = "{x}"')
    s = Solution()
    r = s.isValid(x)
    print(f' Output: {r}')


@cli.command()
def merge_two_sorted_lists() -> None:
    """21# Merge Two Sorted Lists."""
    from leetcode.merge_two_sorted_lists import Solution
    from leetcode.utils.singly_linked_list import build, dump

    nums1, nums2 = [1, 2, 4], [1, 3, 4]
    print(f' Input: l1 = {nums1}, l2 = {nums2}')
    l1, l2 = build(nums1), build(nums2)
    s = Solution()
    x = s.mergeTwoLists(l1, l2)
    res = dump(x)
    print(f' Output: {res}')


@cli.command()
def generate_parentheses() -> None:
    """22# Generate Parentheses."""
    from leetcode.generate_parentheses import Solution

    n = 3
    print(f' Input: n = {n}')
    s = Solution()
    x = s.generateParenthesis(n)
    print(f' Output: {x}')


@cli.command()
def merge_k_sorted_lists() -> None:
    """23# Merge k Sorted Lists."""
    from leetcode.merge_k_sorted_lists import Solution
    from leetcode.utils.singly_linked_list import build, dump

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(f' Input: lists = {lists}')
    s = Solution()
    x = []
    for nums in lists:
        head = build(nums)
        x.append(head)
    head = s.mergeKLists(x)
    r = dump(head)
    print(f' Output: {r}')


@cli.command()
def swap_nodes_in_pairs() -> None:
    """24# Swap Nodes in Pairs."""
    from leetcode.swap_nodes_in_pairs import Solution
    from leetcode.utils.singly_linked_list import build, dump

    nums = [1, 2, 3, 4]
    print(f' Input: {nums}')
    head = build(nums)
    s = Solution()
    x = s.swapPairs(head)
    r = dump(x)
    print(f' Output: {r}')


@cli.command()
def reverse_nodes_in_k_group() -> None:
    """25# Reverse Nodes in k-Group."""
    from leetcode.reverse_nodes_in_k_group import Solution
    from leetcode.utils.singly_linked_list import build, dump

    nums, k = [1, 2, 3, 4, 5], 2
    print(f' Input: head = {nums}, k = {k}')
    head = build(nums)
    s = Solution()
    x = s.reverseKGroup(head, k)
    r = dump(x)
    print(f' Output: {r}')


@cli.command()
def remove_duplicates_from_sorted_array() -> None:
    """26# Remove Duplicates from Sorted Array."""
    from leetcode.remove_duplicates_from_sorted_array import Solution

    nums = [1, 1, 2]
    print(f' Input: nums = {nums}')
    s = Solution()
    n = s.removeDuplicates(nums)
    r = nums[:n]
    print(f' Output: {n}, nums = {r}')


@cli.command()
def remove_element() -> None:
    """27# Remove Element."""
    from leetcode.remove_element import Solution

    nums, val = [3, 2, 2, 3], 3
    print(f' Input: nums = {nums}, val = {val}')
    s = Solution()
    x = s.removeElement(nums, val)
    r = nums[:x]
    print(f' Output: {r}')


@cli.command()
def implement_strstr() -> None:
    """28# Implement strStr()."""
    from leetcode.implement_strstr import Solution

    haystack, needle = 'hello', 'll'
    print(f' Input: haystack = {haystack}, needle = {needle}')
    s = Solution()
    r = s.strStr(haystack, needle)
    print(f' Output: {r}')


@cli.command()
def divide_two_integers() -> None:
    """29# Divide Two Integers."""
    from leetcode.divide_two_integers import Solution

    dividend, divisor = 10, 3
    print(f' Input: dividend = {dividend}, divisor = {divisor}')
    s = Solution()
    x = s.divide(dividend, divisor)
    print(f' Output: {x}')


if __name__ == '__main__':
    cli()
