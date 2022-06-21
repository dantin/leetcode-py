# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.defanging_an_ip_address import Solution
    return Solution()


@pytest.mark.parametrize(
    'address, expected',
    [
        ('1.1.1.1', '1[.]1[.]1[.]1'),
        ('255.100.50.0', '255[.]100[.]50[.]0'),
    ],
)
def test_defang_ip_addr(solution, address, expected):
    actual = solution.defangIPaddr(address)
    assert expected == actual
