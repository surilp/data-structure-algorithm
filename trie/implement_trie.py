from string import ascii_lowercase


class Trie:
    LOWERCASE_MAP = {let: idx for idx, let in enumerate(ascii_lowercase)}

    def __init__(self, flag=False):
        self.data = [None] * len(ascii_lowercase)
        self.flag = flag

    def insert(self, word, idx=0):
        if idx == len(word):
            if not self.flag:
                self.flag = True
            return
        let = word[idx]
        let_idx = Trie.LOWERCASE_MAP[let]
        if not self.data[let_idx]:
            self.data[let_idx] = Trie()
        self.data[let_idx].insert(word, idx + 1)

    def search(self, word, idx=0):
        if idx == len(word):
            return self.flag
        let = word[idx]
        let_idx = Trie.LOWERCASE_MAP[let]
        if self.data[let_idx]:
            return self.data[let_idx].search(word, idx + 1)
        else:
            return False

    def starts_with(self, word, idx = 0):
        if idx == len(word):
            return True
        let = word[idx]
        let_idx = Trie.LOWERCASE_MAP[let]
        if self.data[let_idx]:
            return self.data[let_idx].starts_with(word, idx + 1)
        else:
            return False

    def list_of_words_start_with(self, word):
        if len(word) < 2:
            raise Exception('word len should be more than 2')
        result = []
        self.list_of_words_helper(word, 0, result)
        return result


    def list_of_words_helper(self, word, idx, result):
        if idx == len(word):
            return self.get_words(word, self, [], result)
        let = word[idx]
        let_idx = Trie.LOWERCASE_MAP[let]
        if self.data[let_idx]:
            return self.data[let_idx].list_of_words_helper(word, idx + 1, result)
        else:
            return result

    def get_words(self, word, trie, ds, result):
        if trie.flag:
            result.append(word + ''.join(ds))

        if len(result) == 3:
            return True

        for let, idx in Trie.LOWERCASE_MAP.items():
            if trie.data[idx]:
                ds.append(let)
                if self.get_words(word, trie.data[idx], ds, result):
                    return True
                ds.pop()
        return False



    def __str__(self):
        return f'flag = {self.flag}, data = {str(self.data)}'

    def __repr__(self):
        return f'flag = {self.flag}, data = {str(self.data)}'


main = Trie()
main.insert("apple")
main.insert("apps")
main.insert("apps")
main.insert("apxl")
main.insert("bac")
main.insert("bat")
print(main.search('apple'))
print(main.search('apples'))
print(main.search('ba'))
print(main.search('bat'))
print(main.search('apxl'))
print(main.starts_with('batt'))
print(main.list_of_words_start_with('ap'))
s = 1
