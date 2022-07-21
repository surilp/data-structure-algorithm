from __future__ import annotations
from typing import List


class Node:

    def __init__(self):
        self.data: List[Node] = [None] * 26
        self.ends_with_count = 0
        self.starts_with_count = 0

    def get(self, let) -> Node:
        let_idx = self._get_idx(let)
        if self.data[let_idx]:
            return self.data[let_idx]

    def contains(self, let) -> bool:
        let_idx = self._get_idx(let)
        if self.data[let_idx]:
            return True
        return False

    def set(self, let) -> bool:
        let_idx = self._get_idx(let)
        if not self.data[let_idx]:
            self.data[let_idx] = Node()
        return self.data[let_idx]

    def _get_idx(self, let) -> int:
        return ord(let) - ord('a')

    def __str__(self):
        return f'ends with count = {self.ends_with_count}, starts with count = {self.starts_with_count}, data = {[chr(idx + ord("a")) for idx in range(len(self.data)) if self.data[idx]]}'

    def __repr__(self):
        return self.__str__()


class Trie:

    def __init__(self, words):
        self.root = Node()
        self.words = words
        self.insert_word(words)

    def insert(self, word):
        current_node = self.root
        for let in word:
            new_node = current_node.get(let)
            if new_node:
                new_node.starts_with_count += 1
                current_node = new_node
            else:
                current_node = current_node.set(let)
        current_node.ends_with_count += 1

    def insert_word(self, words):
        for word in words:
            self.insert(word)

    def longest_complete_string(self):
        result = ''
        for word in self.words:
            if len(word) > len(result) and self.check_if_word_all_prefix_contain(word):
                result = word if len(word) > len(result) else result
        return result

    def check_if_word_all_prefix_contain(self, word):
        current_node = self.root
        for let in word:
            new_node = current_node.get(let)
            if new_node and new_node.ends_with_count > 0:
                current_node = new_node
            else:
                return False
        return current_node.ends_with_count > 0


words = ['n', 'ninja', 'ninj', 'ni', 'nin', 'ninga']

trie = Trie(words)
print(trie.longest_complete_string())
