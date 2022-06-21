# -*- coding: utf-8 -*-

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
