'''
9 = 0000...1001

XOR = 1^0 =1
1^1 = 0

even number of 1s gives 0
odd number of 1s gives 1

how to check if bit is set or not = (num >> i) & 1 != 0 - set
how to turn on particular bit = 0000.1001 num |(1 << 2)
'''

'''
insert all numbers in terms of binary bits in trie
take x and find the max no form array where no ^ x is maximum

'''


class Node:

    def __init__(self):
        self.data = [None, None]

    def set(self, bit):
        if not self.data[bit]:
            self.data[bit] = Node()
        return self.data[bit]

    def get_bit(self, bit):
        if self.data[bit]:
            return self.data[bit]


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, num):
        current = self.root
        for idx in range(31, -1, -1):
            curr_bit = self._is_bit_set(num, idx)
            current = current.set(curr_bit)

    def insert_nums(self, nums):
        for num in nums:
            self.insert(num)

    def max_xor(self, num):
        result = 0
        current = self.root
        for idx in range(31, -1, -1):
            curr_bit = self._is_bit_set(num, idx)
            new = current.get_bit(1 - curr_bit)
            if new:
                current = new
                result = self._set_bit(result, idx)
            else:
                current = current.get_bit(curr_bit)
        return result

    def _is_bit_set(self, num, shift):
        return (num >> shift) & 1

    def _set_bit(self, num, shift):
        return num | (1 << shift)


nums = [9, 8, 7, 5, 4]
t = Trie()
t.insert_nums(nums)
print(t.max_xor(8))


def max_xor(arr1, arr2):
    t = Trie()
    t.insert_nums(arr1)
    result = -float('inf')
    for num in arr2:
        result = max(result, t.max_xor(num))
    return result


arr1 = [6, 8]
arr2 = [7, 8, 2]
print(max_xor(arr1, arr2))

arr1 = [1, 2]
arr2 = [1, 1]
print(max_xor(arr1, arr2))
