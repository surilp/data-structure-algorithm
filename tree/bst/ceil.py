from tree.Tree import Tree


class Ceil(Tree):

    def __init__(self, data):
        super(Ceil, self).__init__(data)

    def ceil(self, key):
        current = self.root
        result = -1
        while current:
            if current.val == key:
                return key
            elif current.val > key:
                result = current.val
                current = current.left
            else:
                current = current.right
        return result


data = [10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9]
print(Ceil(data).ceil(8))
data = [10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9]
print(Ceil(data).ceil(11))
data = [10, 5, 13, 3, 6, 11, 14, 2, 4, None, 9]
print(Ceil(data).ceil(12))
