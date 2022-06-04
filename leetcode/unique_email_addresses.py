# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        cache = set()
        for email in emails:
            name, domain = email.split('@')
            name = name.split('+', 1)[0]
            name = name.replace('.', '')
            cache.add(f'{name}@{domain}')
        return len(cache)
