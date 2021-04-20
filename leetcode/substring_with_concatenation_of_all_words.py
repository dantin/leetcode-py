# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_cnt = len(words)
        word_freq = defaultdict(int)
        for w in words:
            word_freq[w] += 1

        res = []
        for i in range(word_len):
            cur_word_cnt = 0
            cur_word_freq = defaultdict(int)

            left, right = i, i
            while right + word_len <= len(s):
                w = s[right:right + word_len]
                right += word_len

                if w not in word_freq:
                    left = right
                    cur_word_freq.clear()
                    cur_word_cnt = 0
                else:
                    cur_word_freq[w] += 1
                    cur_word_cnt += 1
                    while cur_word_freq[w] > word_freq[w]:
                        left_word = s[left:left + word_len]
                        left += word_len
                        cur_word_freq[left_word] -= 1
                        cur_word_cnt -= 1
                    if cur_word_cnt == word_cnt:
                        res.append(left)
        return res
