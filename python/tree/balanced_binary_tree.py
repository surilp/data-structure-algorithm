from tree.Tree import Tree

'''
height of left - height of right <= 1
'''

balanced = {
    "nodes": [
        {"id": "1", "left": 9, "right": 20, "value": 3},
        {"id": "2", "left": 15, "right": 7, "value": 20}
    ],
    "root": 3
}

unbalanced = {
    "nodes": [
        {"id": "1", "left": 3, "right": 2, "value": 1},
        {"id": "2", "left": 5, "right": 4, "value": 3},
        {"id": "2", "left": 7, "right": 6, "value": 5}
    ],
    "root": 1
}


class BalancedBinaryTree(Tree):

    def __init__(self, data):
        super().__init__(data)

    def is_balanced(self):
        if not self._is_balanced(self.root):
            return False
        return True

    def _is_balanced(self, node):
        if node:
            left_height = self._is_balanced(node.left)
            right_height = self._is_balanced(node.right)
            if left_height is False or right_height is False:
                return False
            if abs(left_height - right_height) > 1:
                return False
            return 1 + max(left_height, right_height)

        else:
            return 0


print(BalancedBinaryTree(balanced).is_balanced())
print(BalancedBinaryTree(unbalanced).is_balanced())
