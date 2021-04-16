# -*- coding -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.remove_element import Solution
    return Solution()


@pytest.mark.parametrize(
    'nums,val,expected',
    [
        ([3, 2, 2, 3], 2, [3, 3]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 3, 0, 4]),
    ],
)
def test_remove_element(solution, nums, val, expected):
    actual = solution.removeElement(nums, val)
    assert actual == len(expected)
    assert expected == nums[:actual]
