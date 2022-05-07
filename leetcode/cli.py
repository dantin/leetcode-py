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
def tag_validator() -> None:
    """591# Tag Validator."""
    from leetcode.tag_validator import Solution

    code = '<DIV>This is the first line <![CDATA[<div>]]></DIV>'
    print(f' Input: "{code}"')
    s = Solution()
    x = s.isValid(code)
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
def binary_gap() -> None:
    """868# Binary Gap."""
    from leetcode.binary_gap import Solution

    n = 22
    print(f' Input: n = {n}')
    s = Solution()
    x = s.binaryGap(n)
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
def find_the_winner_of_the_circular_game() -> None:
    """1823# Find the Winner of the Circular Game."""
    from leetcode.find_the_winner_of_the_circular_game import Solution

    n, k = 5, 2
    print(f' Input: n = {n}, k = {k}')
    s = Solution()
    x = s.findTheWinner(n, k)
    print(f' Output: {x}')
