# -*- coding: utf-8 -*-
import pytest


@pytest.fixture
def codec():
    from leetcode.serialize_and_deserialize_bst import Codec
    return Codec()


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([2, 1, 3], '2,1,3'),
        ([], ''),
    ],
)
def test_serialize_and_deserialize(codec, nums, expected):
    data = ','.join(str(n) for n in nums)
    root = codec.deserialize(data)
    actual = codec.serialize(root)
    assert expected == actual
