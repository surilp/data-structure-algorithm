from tree.Tree import Tree


class Floor(Tree):

    def __init__(self, data):
        super(Floor, self).__init__(data)

    def floor(self, key):
        current = self.root
        result = -1
        while current:
            if current.val == key:
                return key
            elif current.val > key:
                current = current.left
            else:
                result = current.val
                current = current.right
        return result


data = [10, 5, 15, 2, 6]
print(Floor(data).floor(7))
data = [10, 5, 15, 2, 6]
print(Floor(data).floor(14))
