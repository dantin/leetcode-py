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


@cli.command()
def substring_with_concatenation_of_all_words() -> None:
    """30# Substring with Concatenation of All Words."""
    from leetcode.substring_with_concatenation_of_all_words import Solution

    x, words = 'barfoothefoobarman', ['foo', 'bar']
    print(f' Input: s = "{x}", words = {words}')
    s = Solution()
    r = s.findSubstring(x, words)
    print(f' Output: {r}')


@cli.command()
def next_permutation() -> None:
    """31# Next Permutation."""
    from leetcode.next_permutation import Solution

    nums = [1, 2, 3]
    print(f' Input: nums = {nums}')
    s = Solution()
    s.nextPermutation(nums)
    print(f' Output: {nums}')


@cli.command()
def longest_valid_parentheses() -> None:
    """32# Longest Valid Parentheses."""
    from leetcode.longest_valid_parentheses import Solution

    x = '(()'
    print(f' Input: s = "{x}"')
    s = Solution()
    r = s.longestValidParentheses(x)
    print(f' Output: {r}')


@cli.command()
def search_in_rotated_sorted_array() -> None:
    """33# Search in Rotated Sorted Array."""
    from leetcode.search_in_rotated_sorted_array import Solution

    nums, target = [4, 5, 6, 7, 0, 1, 2], 0
    print(f' Input: nums = {nums}, target = {target}')
    s = Solution()
    x = s.search(nums, target)
    print(f' Output: {x}')


@cli.command()
def find_first_and_last_position_of_element_in_sorted_array() -> None:
    """34# Find First and Last Position of Element in Sorted Array."""
    from leetcode.find_first_and_last_position_of_element_in_sorted_array import Solution

    nums, target = [5, 7, 7, 8, 8, 10], 8
    print(f' Input: nums = {nums}, target = {target}')
    s = Solution()
    x = s.searchRange(nums, target)
    print(f' Output: {x}')


@cli.command()
def search_insert_position() -> None:
    """35# Search Insert Position."""
    from leetcode.search_insert_position import Solution

    nums, target = [1, 3, 5, 6], 5
    print(f' Input: nums = {nums}, target = {target}')
    s = Solution()
    x = s.searchInsert(nums, target)
    print(f' Output: {x}')


@cli.command()
def valid_sudoku() -> None:
    """36# Valid Sudoku."""
    from leetcode.valid_sudoku import Solution

    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    line = '\n,'.join([f'{row}' for row in board])
    print(f' Input: board = \n[{line}]')
    s = Solution()
    x = s.isValidSudoku(board)
    print(f' Output: {x}')


@cli.command()
def sudoku_solver() -> None:
    """37# Sudoku Solver."""
    from leetcode.sudoku_solver import Solution

    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    line = '\n,'.join([f'{row}' for row in board])
    print(f' Input: board = \n[{line}]')
    s = Solution()
    s.solveSudoku(board)
    line = '\n,'.join([f'{row}' for row in board])
    print(f' Output:\n[{line}]')


@cli.command()
def count_and_say() -> None:
    """38# Count and Say."""
    from leetcode.count_and_say import Solution

    n = 4
    print(f' Input: n = {n}')
    s = Solution()
    x = s.countAndSay(n)
    print(f' Output: {x}')


@cli.command()
def combination_sum() -> None:
    """39# Combination Sum."""
    from leetcode.combination_sum import Solution

    candidates, target = [2, 3, 6, 7], 7
    print(f' Input: candidates = {candidates}, target = {target}')
    s = Solution()
    x = s.combinationSum(candidates, target)
    print(f' Output: {x}')


@cli.command()
def combination_sum_ii() -> None:
    """40# Combination Sum II."""
    from leetcode.combination_sum_ii import Solution

    candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
    print(f' Input: candidates = {candidates}, target = {target}')
    s = Solution()
    x = s.combinationSum2(candidates, target)
    print(f' Output: {x}')


@cli.command()
def first_missing_positive() -> None:
    """41# First Missing Positive."""
    from leetcode.first_missing_positive import Solution

    nums = [1, 2, 0]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.firstMissingPositive(nums)
    print(f' Output: {x}')


@cli.command()
def trapping_rain_water() -> None:
    """42# Trapping Rain Water."""
    from leetcode.trapping_rain_water import Solution

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f' Input: height = {height}')
    s = Solution()
    x = s.trap(height)
    print(f' Output: {x}')


@cli.command()
def multiply_strings() -> None:
    """43# Multiply Strings."""
    from leetcode.multiply_strings import Solution

    num1, num2 = '2', '3'
    print(f' Input: num1 = "{num1}, num2 = "{num2}"')
    s = Solution()
    x = s.multiply(num1, num2)
    print(f' Output: {x}')


@cli.command()
def wildcard_matching() -> None:
    """44# Wildcard Matching."""
    from leetcode.wildcard_matching import Solution

    s, p = 'aa', 'a'
    print(f' Input: s = {s}, p = {p}')
    x = Solution()
    r = x.isMatch(s, p)
    print(f' Output: {r}')


@cli.command()
def jump_game_ii() -> None:
    """45# Jump Game II."""
    from leetcode.jump_game_ii import Solution

    nums = [2, 3, 1, 1, 4]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.jump(nums)
    print(f' Output: {x}')


@cli.command()
def permutations() -> None:
    """46# Permutations."""
    from leetcode.permutations import Solution

    nums = [1, 2, 3]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.permute(nums)
    print(f' Output: {x}')


@cli.command()
def permutations_ii() -> None:
    """47# Permutations II."""
    from leetcode.permutations_ii import Solution

    nums = [1, 2, 3]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.permuteUnique(nums)
    print(f' Output: {x}')


@cli.command()
def rotate_image() -> None:
    """48# Rotate Image."""
    from leetcode.rotate_image import Solution

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f' Input: matrix = {matrix}')
    s = Solution()
    s.rotate(matrix)
    print(f' Output: {matrix}')


@cli.command()
def group_anagrams() -> None:
    """49# Group Anagrams."""
    from leetcode.group_anagrams import Solution

    strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    print(f' Input: strs = {strs}')
    s = Solution()
    x = s.groupAnagrams(strs)
    print(f' Output: {x}')


@cli.command()
def powx_n() -> None:
    """50# Pow(x, n)."""
    from leetcode.powx_n import Solution

    x, n = 2.0, 10
    print(f' Input: x = {x}, n = {n}')
    s = Solution()
    ans = s.myPow(x, n)
    print(f' Output: {ans}')


@cli.command()
def n_queens() -> None:
    """51# N Queens."""
    from leetcode.n_queens import Solution

    n = 4
    print(f' Input: n = {n}')
    s = Solution()
    x = s.solveNQueens(n)
    print(f' Output: {x}')


@cli.command()
def n_queens_ii() -> None:
    """52# N Queens II."""
    from leetcode.n_queens_ii import Solution

    n = 4
    print(f' Input: n = {n}')
    s = Solution()
    x = s.totalNQueens(n)
    print(f' Output: {x}')


@cli.command()
def maximum_subarray() -> None:
    """53# Maximum Subarray."""
    from leetcode.maximum_subarray import Solution

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.maxSubArray(nums)
    print(f' Output: {x}')


@cli.command()
def spiral_matrix() -> None:
    """54# Spiral Matrix."""
    from leetcode.spiral_matrix import Solution

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f' Input: matrix = {matrix}')
    s = Solution()
    x = s.spiralOrder(matrix)
    print(f' Output: {x}')


@cli.command()
def jump_game() -> None:
    """55# Jump Game."""
    from leetcode.jump_game import Solution

    nums = [2, 3, 1, 1, 4]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.canJump(nums)
    print(f' Output: {x}')


@cli.command()
def merge_intervals() -> None:
    """56# Merge Intervals."""
    from leetcode.merge_intervals import Solution

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(f' Input: intervals = {intervals}')
    s = Solution()
    x = s.merge(intervals)
    print(f' Output: {x}')


@cli.command()
def insert_interval() -> None:
    """57# Insert Interval."""
    from leetcode.insert_interval import Solution

    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(f' Input: intervals = {intervals}, newInterval = {newInterval}')
    s = Solution()
    x = s.insert(intervals, newInterval)
    print(f' Output: {x}')


@cli.command()
def permutation_sequence() -> None:
    """60# Permutation Sequence."""
    from leetcode.permutation_sequence import Solution

    n = 3
    k = 3
    print(f' Input: n = {n}, k = {k}')
    s = Solution()
    x = s.getPermutation(n, k)
    print(f' Output: {x}')


@cli.command()
def random_pick_index() -> None:
    """398# Random Pick Index."""
    from leetcode.random_pick_index import Solution

    nums = [1, 2, 3, 3, 3]
    print(f' Input: nums = {nums}')
    s = Solution(nums)
    x = s.pick(1)
    print(f' Output: {x}')


@cli.command()
def pacific_atlantic_water_flow() -> None:
    """417# Pacific Atlantic Water Flow."""
    from leetcode.pacific_atlantic_water_flow import Solution

    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]]
    print(f' Input: heights = {heights}')
    s = Solution()
    x = s.pacificAtlantic(heights)
    print(f' Output: {x}')


@cli.command()
def construct_quad_tree() -> None:
    """427: Construct Quad Tree."""
    from leetcode.construct_quad_tree import Solution
    from leetcode.utils.quad_tree import dump

    grid = [[0, 1], [1, 0]]
    print(f' Input: grid = {grid}')
    s = Solution()
    x = s.construct(grid)
    out = dump(x)
    print(f' Output: {out}')


@cli.command()
def minimum_genetic_mutation() -> None:
    """433# Minimum Genetic Mutation."""
    from leetcode.minimum_genetic_mutation import Solution

    start = 'AACCGGTT'
    end = 'AACCGGTA'
    bank = ['AACCGGTA']
    print(f' Input: start = {start}, end = {end}, bank = {bank}')
    s = Solution()
    x = s.minMutation(start, end, bank)
    print(f' Output: {x}')


@cli.command()
def find_right_interval() -> None:
    """436# Find Right Interval."""
    from leetcode.find_right_interval import Solution

    intervals = [[1, 2]]
    print(f' Input: intervals = {intervals}')
    s = Solution()
    x = s.findRightInterval(intervals)
    print(f' Output: {x}')


@cli.command()
def find_all_duplicates_in_an_array() -> None:
    """442# Find All Duplicates in An Array."""
    from leetcode.find_all_duplicates_in_an_array import Solution

    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.findDupicates(nums)
    print(f' Output: {x}')


@cli.command()
def serialize_and_deserialize_bst() -> None:
    """449# Serialize and Deserialize Binary Search Tree."""
    from leetcode.serialize_and_deserialize_bst import Codec

    nums = [2, 1, 3]
    print(f' Input: root = {nums}')
    codec = Codec()
    root = codec.deserialize(','.join(str(n) for n in nums))
    raw = codec.serialize(root)
    print(f' Input: [{raw}]')


@cli.command()
def delete_node_in_a_bst() -> None:
    """450# Delete Node in a Binary Search Tree."""
    from leetcode.delete_node_in_a_bst import Solution
    from leetcode.utils.binary_search_tree import make_tree, dump_tree

    nums = [5, 3, 6, 2, 4, None, 7]
    key = 3
    print(f' Input: root = {nums}, key = {key}')
    root = make_tree(nums, 0)
    s = Solution()
    root = s.deleteNode(root, key)
    x = dump_tree(root)
    print(f' Output: {x}')


@cli.command()
def minimum_moves_to_equal_array_elements_ii() -> None:
    """462# Minimum Moves to Equal Array Elements II."""
    from leetcode.minimum_moves_to_equal_array_elements_ii import Solution

    nums = [1, 2, 3]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.minMoves2(nums)
    print(f' Output: {x}')


@cli.command()
def can_i_win() -> None:
    """464# Can I Win."""
    from leetcode.can_i_win import Solution

    max_choosible_integer = 10
    desired_total = 11
    print(f' Input: maxChoosableInteger = {max_choosible_integer}, desiredTotal = {desired_total}')
    s = Solution()
    x = s.canIWin(max_choosible_integer, desired_total)
    print(f' Output: {x}')


@cli.command()
def unique_substrings_in_wraparound_string() -> None:
    """467# Unique Substrings in Wraparound String."""
    from leetcode.unique_substrings_in_wraparound_string import Solution

    p = 'a'
    print(f' Input: p = "{p}"')
    s = Solution()
    x = s.findSubstringInWraproundString(p)
    print(f' Output: {x}')


@cli.command()
def validate_ip_address() -> None:
    """468# Validate IP Address."""
    from leetcode.validate_ip_address import Solution

    queryIP = '172.16.254.1'
    print(f' Input: queryIP = "{queryIP}"')
    s = Solution()
    x = s.validIPAddress(queryIP)
    print(f' Output: "{x}"')


@cli.command()
def matchsticks_to_square() -> None:
    """473# Matchsticks to Square."""
    from leetcode.matchsticks_to_square import Solution

    matchsticks = [1, 1, 2, 2, 2]
    print(f' Input: matchsticks = {matchsticks}')
    s = Solution()
    x = s.makesquare(matchsticks)
    print(f' Output: {x}')


@cli.command()
def generate_random_point_in_a_circle() -> None:
    """478# Generate Random Point in a Circle."""
    from leetcode.generate_random_point_in_a_circle import Solution

    cmds = ['Solution', 'randPoint', 'randPoint', 'randPoint']
    params = [[1.0, 0.0, 0.0], [], [], []]
    print(f'Input:\n{cmds}\n{params}')
    s = Solution(*params[0])
    output = [None]
    for cmd, param in zip(cmds, params):
        if cmd == 'randPoint':
            x = s.randPoint()
            output.append(x)
    print(f'Output:\n{output}')


@cli.command()
def random_point_in_non_overlapping_rectangles() -> None:
    """497. Random Point in Non-overlapping Rectangles."""
    from leetcode.random_point_in_non_overlapping_rectangles import Solution

    cmds = ['Solution', 'pick', 'pick', 'pick', 'pick', 'pick']
    params = [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
    print(f'Input:\n{cmds}')
    s = Solution(*params[0])
    output = [None]
    for cmd, param in zip(cmds, params):
        if cmd == 'pick':
            x = s.pick()
            output.append(x)
    print(f'Output:\n{output}')


@cli.command()
def diagonal_traverse() -> None:
    """498# Diagonal Traverse."""
    from leetcode.diagonal_traverse import Solution

    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f' Input: mat = {mat}')
    s = Solution()
    x = s.findDiagonalOrder(mat)
    print(f' Output: {x}')


@cli.command()
def most_frequent_substree_sum() -> None:
    """508: Most Frquent Subtree Sum."""
    from leetcode.most_frequent_subtree_sum import Solution
    from leetcode.utils.binary_search_tree import make_tree

    nums = [5, 2, -3]
    print(f' Input: {nums}')
    root = make_tree(nums, 0)
    s = Solution()
    x = s.findFrequentTreeSum(root)
    print(f' Output: {x}')


@cli.command()
def find_bottom_left_tree_value() -> None:
    """513# Find Bottom Left Tree Value."""
    from leetcode.find_bottom_left_tree_value import Solution
    from leetcode.utils.binary_search_tree import make_tree

    nums = [2, 1, 3]
    print(f' Input: root = {nums}')
    root = make_tree(nums, 0)
    s = Solution()
    x = s.findBottomLeftValue(root)
    print(f' Output: {x}')


@cli.command()
def find_largest_value_in_each_tree_row() -> None:
    """515# Find Largetst Value in Each Tree Row."""
    from leetcode.find_largest_value_in_each_tree_row import Solution
    from leetcode.utils.binary_search_tree import make_tree

    nums = [1, 3, 2, 5, 3, None, 9]
    print(f' Input: root = {nums}')
    root = make_tree(nums, 0)
    s = Solution()
    x = s.largestValues(root)
    print(f' Output: {x}')


@cli.command()
def k_diff_pairs_in_an_array() -> None:
    """532# K Diff Pairs in an Array."""
    from leetcode.k_diff_pairs_in_an_array import Solution

    nums = [3, 1, 4, 1, 5]
    k = 2
    print(f' Input: nums = {nums}, k = {k}')
    s = Solution()
    x = s.findPairs(nums, k)
    print(f' Output: {x}')


@cli.command()
def tag_validator() -> None:
    """591# Tag Validator."""
    from leetcode.tag_validator import Solution

    code = '<DIV>This is the first line <![CDATA[<div>]]></DIV>'
    print(f' Input: "{code}"')
    s = Solution()
    x = s.isValid(code)
    print(f' Output: {x}')


@cli.command()
def kth_smallest_number_in_multiplication_table() -> None:
    """668# Kth Smallest Number in Multiplication Table."""
    from leetcode.kth_smallest_number_in_multiplication_table import Solution

    m, n = 3, 3
    k = 5
    print(f' Input: m = {m}, n = {n}, k = {k}')
    s = Solution()
    x = s.findKthNumber(m, n, k)
    print(f' Output: {x}')


@cli.command()
def cut_off_trees_for_golf_event() -> None:
    """675# Cut Off Trees for Golf Event."""
    from leetcode.cut_off_trees_for_golf_event import Solution

    forest = [[1, 2, 3], [0, 0, 4], [7, 6, 5]]
    print(f' Input: forest = {forest}')
    s = Solution()
    x = s.cutOffTree(forest)
    print(f' Output: {x}')


@cli.command()
def stickers_to_spell_word() -> None:
    """691# Stickers to Spell Word."""
    from leetcode.stickers_to_spell_word import Solution

    stickers = ['with', 'example', 'science']
    target = 'thehat'
    print(f' Input: stickers = {stickers}, target = {target}')
    s = Solution()
    x = s.minStickers(stickers, target)
    print(f' Output: {x}')


@cli.command()
def falling_squares() -> None:
    """699# Falling Squares."""
    from leetcode.falling_squares import Solution

    positions = [[1, 2], [2, 3], [6, 1]]
    print(f' Input: positions = {positions}')
    s = Solution()
    x = s.fallingSquares(positions)
    print(f' Output: {x}')


@cli.command()
def subarray_product_less_than_k() -> None:
    """713# Subarray Product Less Than K."""
    from leetcode.subarray_product_less_than_k import Solution

    nums, k = [10, 5, 2, 6], 100
    print(f' Input: nums = {nums}, k = {k}')
    s = Solution()
    x = s.numSubarrayProductLessThanK(nums, k)
    print(f' Output: {x}')


@cli.command()
def range_module() -> None:
    """715# Range Module."""
    from leetcode.range_module import RangeModule
    cmds = ['RangeModule', 'addRange', 'removeRange', 'queryRange', 'queryRange', 'queryRange']
    params = [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
    print(f'Input:\n{cmds}\n{params}')

    s = RangeModule()
    output = [None]
    for cmd, param in zip(cmds, params):
        if cmd == 'addRange':
            x = s.addRange(*param)
        elif cmd == 'removeRange':
            x = s.removeRange(*param)
        elif cmd == 'queryRange':
            x = s.queryRange(*param)
        else:
            continue
        output.append(x)
    print(f'Output:\n{output}')


@cli.command()
def find_k_th_smallest_pair_distance() -> None:
    """719# Find Kth Smallest Pair Distance."""
    from leetcode.find_k_th_smallest_pair_distance import Solution

    nums = [1, 3, 1]
    k = 1
    print(f' Input: nums = {nums}, k = {k}')
    s = Solution()
    x = s.smallestDistancePair(nums, k)
    print(f' Output: {x}')


@cli.command()
def count_different_palindromic_subsequences() -> None:
    """730# Count Different Palindromic Subsequences."""
    from leetcode.count_different_palindromic_subsequences import Solution

    s = 'bccb'
    print(f' Input: s = {s}')
    solution = Solution()
    x = solution.countPalindromicSubsequences(s)
    print(f' Output: {x}')


@cli.command()
def my_calendar_iii() -> None:
    """732# My Calendar III."""
    from leetcode.my_calendar_iii import MyCalendarThree

    cmds = ['MyCalendarThree', 'book', 'book', 'book', 'book', 'book', 'book']
    params = [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    print(f'Input:\n{cmds}\n{params}')

    s = MyCalendarThree()
    output = [None]
    for cmd, param in zip(cmds, params):
        if cmd == 'book':
            x = s.book(*param)
            output.append(x)
    print(f'Output:\n{output}')


@cli.command()
def largest_triangle_area() -> None:
    """812# Largest Triangle Area."""
    from leetcode.largest_triangle_area import Solution

    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(f' Input: points = {points}')
    s = Solution()
    x = s.largestTriangleArea(points)
    print(f' Output: {x}')


@cli.command()
def consecutive_numbers_sum() -> None:
    """829# Consecutive Numbers Sum."""
    from leetcode.consecutive_numbers_sum import Solution

    n = 5
    print(f' Input: n = {n}')
    s = Solution()
    x = s.consecutiveNumbersSum(n)
    print(f' Output: {x}')


@cli.command()
def binary_gap() -> None:
    """868# Binary Gap."""
    from leetcode.binary_gap import Solution

    n = 22
    print(f' Input: n = {n}')
    s = Solution()
    x = s.binaryGap(n)
    print(f' Output: {x}')


@cli.command()
def koko_eating_bananas() -> None:
    """Koko Eating Bananas."""
    from leetcode.koko_eating_bananas import Solution

    piles = [3, 6, 7, 11]
    h = 8
    print(f' Input: piles = {piles}, h = {h}')
    s = Solution()
    x = s.minEatingSpeed(piles, h)
    print(f' Output: {x}')


@cli.command()
def projection_area_of_3d_shapes() -> None:
    """883# Projection Area of 3D-Shapes."""
    from leetcode.projection_area_of_3d_shapes import Solution

    grid = [[1, 2], [3, 4]]
    print(f' Input: {grid}')
    s = Solution()
    x = s.projectionArea(grid)
    print(f' Output: {x}')


@cli.command()
def sort_array_by_parity() -> None:
    """905# Sort Array by Parity."""
    from leetcode.sort_array_by_parity import Solution

    nums = [3, 1, 2, 4]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.sortArrayByParity(nums)
    print(f' Output: {x}')


@cli.command()
def smallest_range_i() -> None:
    """908# Smallest Range I."""
    from leetcode.smallest_range_i import Solution

    nums, k = [1], 0
    print(f' Input: nums = {nums}, k = {k}')
    s = Solution()
    x = s.smallestRangeI(nums, k)
    print(f' Output: {x}')


@cli.command()
def flip_string_to_monotone_increasing() -> None:
    """926# Flip String to Monotone Increasing."""
    from leetcode.flip_string_to_monotone_increasing import Solution

    s = '00110'
    print(f' Input: s = "{s}"')
    solution = Solution()
    x = solution.minFlipsMonoIncr(s)
    print(f' Output: {x}')


@cli.command()
def unique_email_addresses() -> None:
    """929# Unique Email Addresses."""
    from leetcode.unique_email_addresses import Solution

    emails = ['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com',
              'testemail+david@lee.tcode.com']
    print(f' Input: emails = {emails}')
    s = Solution()
    x = s.numUniqueEmails(emails)
    print(f' Output: {x}')


@cli.command()
def number_of_recent_calls() -> None:
    """933# Number of Recent Calls."""
    from leetcode.number_of_recent_calls import RecentCounter

    commands = ['RecentCounter'] + ['ping'] * 4
    params = [[], [1], [100], [3001], [3002]]
    print(f' Input:\n {commands}\n {params}')
    counter = RecentCounter()
    output = [None]
    for cmd, args in zip(commands, params):
        if cmd == 'ping':
            x = counter.ping(args[0])
            output.append(x)
    print(f' Output:\n {output}')


@cli.command()
def reorder_data_in_log_files() -> None:
    """937# Reorder Data in Log Files."""
    from leetcode.reorder_data_in_log_files import Solution

    logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
    print(f' Input: {logs}')
    s = Solution()
    x = s.reorderLogFiles(logs)
    print(f' Output: {x}')


@cli.command()
def di_string_match() -> None:
    """942# DI String Match."""
    from leetcode.di_string_match import Solution

    s = 'IDID'
    print(f' Input: s = {s}')
    solution = Solution()
    x = solution.diStringMatch(s)
    print(f' Output: {x}')


@cli.command()
def delete_columns_to_make_sorted() -> None:
    """944# Delete Columns to Make Sorted."""
    from leetcode.delete_columns_to_make_sorted import Solution

    strs = ['cba', 'daf', 'ghi']
    print(f' Input: strs = {strs}')
    s = Solution()
    x = s.minDeleteionSize(strs)
    print(f' Output: {x}')


@cli.command()
def verifying_an_alien_dictionary() -> None:
    """953# Verifying An Alien Dictionary."""
    from leetcode.verifying_an_alien_dictionary import Solution

    # words = ['hello', 'leetcode']
    # order = 'hlabcdefgijkmnopqrstuvwxyz'
    words = ["kxvyx", "ts"]
    order = "tiwjpbemkhalsqzdvucorfgxyn"
    print(f' Input: words = {words}, order = {order}')
    s = Solution()
    x = s.isAlienSorted(words, order)
    print(f' Output: {x}')


@cli.command()
def n_repeated_element_in_size_2n_array() -> None:
    """961# N Repeated Element in Size 2N Array."""
    from n_repeated_element_in_size_2n_array import Solution

    nums = [1, 2, 3, 3]
    print(f' Input: nums = {nums}')
    s = Solution()
    x = s.repeatedNTimes(nums)
    print(f' Output: {x}')


@cli.command()
def univalued_binary_tree() -> None:
    """965# Univalued Binary Tree."""
    from leetcode.univalued_binary_tree import Solution
    from leetcode.utils.binary_search_tree import make_tree

    nums = [1, 1, 1, 1, 1, None, 1]
    print(f' Input: {nums}')
    root = make_tree(nums, 0)
    s = Solution()
    x = s.isUnivalTree(root)
    print(f' Output: {x}')


@cli.command()
def remove_outermost_parentheses() -> None:
    """1021# Remove Outermost Parentheses."""
    from leetcode.remove_outermost_parentheses import Solution

    s = '(()())(())'
    print(f' Input: s = "{s}"')
    solution = Solution()
    x = solution.removeOuterParentheses(s)
    print(f' Output: "{x}"')


@cli.command()
def sum_of_root_to_leaf_binary_numbers() -> None:
    """1022# Sum of Root to Leaf Binary Numbers."""
    from leetcode.sum_of_root_to_leaf_binary_numbers import Solution
    from leetcode.utils.binary_search_tree import make_tree

    nums = [1, 0, 1, 0, 1, 0, 1]
    root = make_tree(nums, 0)
    print(f' root = {nums}')
    s = Solution()
    x = s.sumRootToLeaf(root)
    print(f' Output: {x}')


@cli.command()
def valid_boomerang() -> None:
    """1037# Valid Boomerang."""
    from leetcode.valid_boomerang import Solution

    points = [[1, 1], [2, 3], [3, 2]]
    print(f' Input: points = {points}')
    s = Solution()
    x = s.isBoomerang(points)
    print(f' Output: {x}')


@cli.command()
def height_checker() -> None:
    """1051# Height Checker."""
    from leetcode.height_checker import Solution

    heights = [1, 1, 4, 2, 1, 3]
    print(f' Input: heights = {heights}')
    s = Solution()
    x = s.heightChecker(heights)
    print(f' Output: {x}')


@cli.command()
def duplicate_zeros() -> None:
    """1089# Duplicate Zeros."""
    from leetcode.duplicate_zeros import Solution

    nums = [1, 0, 2, 3, 0, 4, 5, 0]
    print(f' Input: {nums}')
    s = Solution()
    s.duplicateZeros(nums)
    print(f' Input: {nums}')


@cli.command()
def defanging_an_ip_address() -> None:
    """1108# Defanging an IP Address."""
    from leetcode.defanging_an_ip_address import Solution

    address = '1.1.1.1'
    print(f' Input: address = {address}')
    s = Solution()
    x = s.defangIPaddr(address)
    print(f' Input: {x}')


@cli.command()
def all_elements_in_two_binary_search_trees() -> None:
    """1305# All Emements in Two Binary Search Trees."""
    from leetcode.all_elements_in_two_binary_search_trees import Solution
    from leetcode.utils.binary_search_tree import make_tree

    nums1, nums2 = [2, 1, 4], [1, 0, 3]
    print(f' Input: root1 = {nums1}, root2 = {nums2}')
    root1 = make_tree(nums1, 0)
    root2 = make_tree(nums2, 0)
    s = Solution()
    x = s.getAllElements(root1, root2)
    print(f' Output: {x}')


@cli.command()
def cat_and_mouse_ii() -> None:
    """1728# Cat and Mouse II."""
    from leetcode.cat_and_mouse_ii import Solution

    grid = ['####F', '#C...', 'M....']
    catJump, mouseJump = 1, 2
    print(f' Input: grid = {grid}, catJump = {catJump}, mouseJump = {mouseJump}')
    s = Solution()
    x = s.canMouseWin(grid, catJump, mouseJump)
    print(f' Output: {x}')


@cli.command()
def find_the_winner_of_the_circular_game() -> None:
    """1823# Find the Winner of the Circular Game."""
    from leetcode.find_the_winner_of_the_circular_game import Solution

    n, k = 5, 2
    print(f' Input: n = {n}, k = {k}')
    s = Solution()
    x = s.findTheWinner(n, k)
    print(f' Output: {x}')


@cli.command()
def one_away_lcci() -> None:
    """01.05. One Away Edit."""
    from leetcode.one_way_lcci import Solution

    first, second = 'pale', 'ple'
    print(f' Input:\n first = {first}\n second = {second}')
    s = Solution()
    x = s.oneEditAway(first, second)
    print(f' Output: {x}')


@cli.command()
def successor_lcci() -> None:
    """04.06. Successor."""
    from leetcode.utils.binary_search_tree import make_tree, find_node
    from leetcode.successor_lcci import Solution

    nums = [2, 1, 3]
    p = 1
    print(f' Input: root = {nums}, p = {p}')
    root = make_tree(nums, 0)
    target = find_node(root, p)
    s = Solution()
    x = s.inorderSucessor(root, target)
    print(f' Output: {x.val}')


@cli.command()
def find_closest_lcci() -> None:
    """17.11. Find Closest."""
    from leetcode.find_closest_lcci import Solution

    words = ['I', 'am', 'a', 'student', 'from', 'a', 'university', 'in', 'a', 'city']
    word1, word2 = 'a', 'student'
    print(f' Input: words = {words}, word1 = {word1}, word2 = {word2}')
    s = Solution()
    x = s.findClosest(words, word1, word2)
    print(f' Output: {x}')


@cli.command()
def sorted_cycle_linked_list() -> None:
    """Offer II 209. Sortd cycle linked list."""
    from leetcode.sorted_cycle_linked_list import Solution
    from leetcode.utils.cycle_linked_list import build, dump

    nums = [3, 4, 1]
    val = 2
    print(f' Input: head = {nums}, insertVal = {val}')
    head = build(nums)

    s = Solution()
    head = s.insert(head, val)
    x = dump(head)
    print(f' Output: {x}')


@cli.command()
def alien_dictionary() -> None:
    """Offer II 114. Alien Dictionary."""
    from leetcode.alien_dictionary import Solution

    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    print(f' Input: words = {words}')
    s = Solution()
    x = s.alienOrder(words)
    print(f' Output: "{x}"')
