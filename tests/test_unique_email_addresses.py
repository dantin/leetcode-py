# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.unique_email_addresses import Solution
    return Solution()


@pytest.mark.parametrize(
    'emails, expected',
    [
        (['test.email+alex@leetcode.com', 'test.e.mail+bob.cathy@leetcode.com',
          'testemail+david@lee.tcode.com'], 2),
        (['a@leetcode.com', 'b@leetcode.com', 'c@leetcode.com'], 3),
    ],
)
def test_num_unique_emails(solution, emails, expected):
    actual = solution.numUniqueEmails(emails)
    assert expected == actual
