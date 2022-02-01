class Node:

    def __init__(self):
        self.data = [None] * 26

    def set(self, let):
        let_idx = ord(let) - ord('a')
        if not self.data[let_idx]:
            self.data[let_idx] = Node()
        return self.data[let_idx]

    def get(self, let):
        let_idx = ord(let) - ord('a')
        if self.data[let_idx]:
            return self.data[let_idx]


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        result = 1
        for idx in range(len(word)):
            result += self._insert(word, idx)
        return result

    def _insert(self, word, idx):
        count = 0
        current_node = self.root
        for c_idx in range(idx, len(word)):
            new_node = current_node.get(word[c_idx])
            if not new_node:
                new_node = current_node.set(word[c_idx])
                count += 1
            current_node = new_node

        return count


t = Trie()
print(t.insert('abab'))




def get_all_substrings(word):
    result = set()
    for idx in range(len(word)):
        _get_all_substrings(word, idx, [], result)
    return result

def _get_all_substrings(word, idx , ds, result):
    if idx < len(word):
        ds.append(word[idx])
        result.add(''.join(ds))
        _get_all_substrings(word, idx+1, ds, result)
        ds.pop()

print(get_all_substrings('abab'))

