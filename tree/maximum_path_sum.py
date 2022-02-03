'''
disregard negative sum coming from left or right

'''

from tree.Tree import Tree


class MaxPath(Tree):

    def __init__(self, data):
        super().__init__(data)

    def max_sum_path(self):
        return self._max_sum_path(self.root)[1]

    def _max_sum_path(self, node):
        if node:
            left, l_max = self._max_sum_path(node.left)
            right, r_max = self._max_sum_path(node.right)
            c_val = node.val
            if left > 0 or right > 0:
                c_val = max(c_val + left, c_val, right)
            return c_val, max(l_max, r_max, node.val + left + right)
        else:
            return 0, 0


data = {
    "nodes": [
        {"id": "1", "left": 9, "right": 20, "value": -10},
        {"id": "2", "left": 15, "right": 7, "value": 20}
    ],
    "root": -10
}
print(MaxPath(data).max_sum_path())

data = {
    "nodes": [
        {"id": "1", "left": 10, "right": 20, "value": 15},
        {"id": "2", "left": -30, "right": -15, "value": 20}
    ],
    "root": 15
}
print(MaxPath(data).max_sum_path())
