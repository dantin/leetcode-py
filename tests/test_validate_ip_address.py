# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.validate_ip_address import Solution
    return Solution()


@pytest.mark.parametrize(
    'queryIP, expected',
    [
        ('172.16.254.1', 'IPv4'),
        ('2001:0db8:85a3:0:0:8A2E:0370:7334', 'IPv6'),
        ('256.256.256.256', 'Neither'),
    ],
)
def test_valid_ip_address(solution, queryIP, expected):
    actual = solution.validIPAddress(queryIP)
    assert expected == actual
