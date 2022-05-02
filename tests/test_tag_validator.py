# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def solution():
    from leetcode.tag_validator import Solution
    return Solution()


@pytest.mark.parametrize(
    'code, expected',
    [
        ("""<DIV>This is the first line <![CDATA[<div>]]></DIV>""", True),
        ("""<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>""", True),
        ("""<A>  <B> </A>   </B>""", False),
        ("""<DIV>  div tag is not closed  <DIV>""", False),
        ("""<DIV>  unmatched <  </DIV>""", False),
        ("""<DIV> closed tags with invalid tag name  <b>123</b> </DIV>""", False),
        ("""<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>""",
            False),
        ("""<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>""", False),
    ],
)
def test_is_valid(solution, code, expected):
    actual = solution.isValid(code)
    assert expected == actual
