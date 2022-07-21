from tree.Tree import Tree


class CountCompleteBinaryTree(Tree):

    def __init__(self, data):
        super().__init__(data)

    def count(self):
        return self._count(self.root)

    def _count(self, node):
        if node:
            left_h = self.left_height(node)
            right_h = self.right_height(node)

            if left_h == right_h:
                return (2 ** left_h) - 1

            left = self._count(node.left)
            right = self._count(node.right)

            return left + right + 1
        return 0

    def left_height(self, node):
        result = 0
        while node:
            result += 1
            node = node.left
        return result

    def right_height(self, node):
        result = 0
        while node:
            result += 1
            node = node.right
        return result


data = [1, 2, 3, 4, 5, 6, 7]
tree = CountCompleteBinaryTree(data)
print(tree.count())

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tree = CountCompleteBinaryTree(data)
print(tree.count())
