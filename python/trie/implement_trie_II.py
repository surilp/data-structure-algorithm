'''
ord() - char to ASCII int
chr() - ASCII int to char
'''
from __future__ import annotations


class Node:

    def __init__(self):
        self.data = [None] * 26
        self.end_with_count = 0
        self.start_with_count = 0

    def get(self, let) -> Node:
        let_idx = self._get_let_index(let)
        if self.data[let_idx]:
            return self.data[let_idx]

    def set(self, let) -> Node:
        let_idx = self._get_let_index(let)
        if self.data[let_idx]:
            return self.data[let_idx]
        else:
            self.data[let_idx] = Node()
            return self.data[let_idx]

    def _get_let_index(self, let):
        return ord(let) - ord('a')

    def __str__(self):
        return f'end_with_count = {self.end_with_count}, start_with_count = {self.start_with_count} and data = {[chr(idx + ord("a")) for idx in range(len(self.data)) if self.data[idx]]}'

    def __repr__(self):
        return self.__str__()


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root
        for let in word:
            new_node = current_node.set(let)
            new_node.start_with_count += 1
            current_node = new_node
        current_node.end_with_count += 1

    def count_words_equal_to(self, word):
        current_node = self.root
        for let in word:
            new_node = current_node.get(let)
            if new_node:
                current_node = new_node
            else:
                return 0
        return current_node.end_with_count

    def count_words_starting_with(self, prefix):
        current_node = self.root
        for let in prefix:
            new_node = current_node.get(let)
            if new_node:
                current_node = new_node
            else:
                return 0
        return current_node.start_with_count

    def erase(self, word):
        if self.count_words_equal_to(word):
            current_node = self.root
            for let in word:
                new_node = current_node.get(let)
                if new_node:
                    new_node.start_with_count -= 1
                    current_node = new_node
                else:
                    return False
            current_node.end_with_count -= 1
            return True
        return False


trie = Trie()
trie.insert('apple')
trie.insert('apple')
trie.insert('apps')
trie.insert('apps')
print(trie.count_words_equal_to('apple'))
print(trie.count_words_equal_to('appl'))
print(trie.count_words_starting_with('appl'))
trie.erase('apple')
print(trie.count_words_equal_to('apple'))
print(trie.count_words_starting_with('app'))
