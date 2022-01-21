'''
offline queries
online queries - sovle the query in the given order
sort according to ai
'''


class Node:

    def __init__(self):
        self.data = [None, None]

    def get(self, bit):
        if self.data[bit]:
            return self.data[bit]

    def set(self, bit):
        if not self.data[bit]:
            self.data[bit] = Node()
        return self.data[bit]


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, num):
        current = self.root
        for idx in range(31, -1, -1):
            bit = self.is_bit_set(num, idx)
            new = current.get(bit)
            if new:
                current = new
            else:
                current = current.set(bit)

    def max_xor(self, num):
        current = self.root
        result = 0
        for idx in range(31, -1, -1):
            bit = self.is_bit_set(num, idx)
            new = current.get(1 - bit)
            if new:
                result = self.set_bit(result, idx)
                current = new
            else:
                current = current.get(bit)
        return result

    def is_bit_set(self, num, idx):
        return (num >> idx) & 1

    def set_bit(self, num, idx):
        return num | (1 << idx)


def max_xor_query(arr, queries):
    arr.sort()
    queries = get_sorted_query(queries)
    result = [None] * len(queries)
    trie = Trie()
    arr_counter = 0
    for main, limit, idx in queries:
        while arr_counter < len(arr) and arr[arr_counter] <= limit:
            trie.insert(arr[arr_counter])
            arr_counter += 1
        if arr_counter == 0:
            result[idx] = -1
        else:
            xor_val = trie.max_xor(main)
            result[idx] = xor_val
    return result


def get_sorted_query(query):
    for idx, item in enumerate(query):
        item.append(idx)
    query.sort(key=lambda x: x[1])
    return query


arr = [0, 1, 2, 3, 4]
queries = [[1, 3], [5, 6]]
print(max_xor_query(arr, queries))

arr = [1]
queries = [[1, 0]]
print(max_xor_query(arr, queries))

arr = [6, 6, 3, 5, 2, 4]
queries = [[6, 3], [8, 1], [12, 4]]
print(max_xor_query(arr, queries))
