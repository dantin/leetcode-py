# -*- coding: utf-8 -*-

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if '.' in queryIP:
            # IPv4
            if is_valid_ipv4(queryIP):
                return 'IPv4'
        else:
            # IPv6
            if is_valid_ipv6(queryIP):
                return 'IPv6'
        return 'Neither'


def is_valid_ipv4(queryIP: str) -> bool:
    last = -1
    for i in range(4):
        cur = (len(queryIP) if i == 3 else queryIP.find('.', last + 1))
        if cur == -1:
            return False
        if not 1 <= cur - last - 1 <= 3:
            return False

        addr = 0
        for j in range(last + 1, cur):
            if not queryIP[j].isdigit():
                return False
            addr = addr * 10 + int(queryIP[j])

        if addr > 255:
            # overflow.
            return False
        if addr > 0 and queryIP[last + 1] == '0':
            # with prefix '0'.
            return False
        if addr == 0 and cur - last - 1 > 1:
            # '00' or '000'.
            return False

        last = cur

    return True


def is_valid_ipv6(queryIP: str) -> bool:
    last = -1
    for i in range(8):
        cur = (len(queryIP) if i == 7 else queryIP.find(':', last + 1))
        if cur == -1:
            return False
        if not 1 <= cur - last - 1 <= 4:
            return False

        for j in range(last + 1, cur):
            if not queryIP[j].isdigit() and not('a' <= queryIP[j].lower() <= 'f'):
                return False

        last = cur

    return True
