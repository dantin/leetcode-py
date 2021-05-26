# -*- coding: utf-8 -*-
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = collections.defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            cache[key].append(s)
        return list(cache.values())
