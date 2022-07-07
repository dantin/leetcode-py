# -*- coding: utf-8 -*-
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> str:
        node = self
        out = ''
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                return word
            out += ch
            node = node.children[idx]
            if node.is_end:
                return out
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        out = []
        for word in sentence.split():
            out.append(trie.search(word))
        return ' '.join(out)
