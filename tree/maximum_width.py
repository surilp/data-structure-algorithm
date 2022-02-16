from tree.Tree import Tree


class MaximumWidth(Tree):

    def __init__(self, data):
        super().__init__(data)

    def MaximumWidth(self):
        return 2 ** (self._maximum_width(self.root) - 1)

    def _maximum_width(self, node):
        if node:
            left = self._maximum_width(node.left)
            right = self._maximum_width(node.right)
            return max(left, right) + 1
        else:
            return 0


data = {
    "nodes": [
        {"id": "1", "left": 3, "right": 2, "value": 1},
        {"id": "2", "left": None, "right": 9, "value": 2},
        {"id": "3", "left": 5, "right": 4, "value": 3}
    ],
    "root": 1
}
print(MaximumWidth(data).MaximumWidth())

data = {
    "nodes": [
        {"id": "1", "left": 3, "right": 2, "value": 1},
        {"id": "2", "left": 5, "right": None, "value": 3}
    ],
    "root": 1
}
print(MaximumWidth(data).MaximumWidth())


data = {
    "nodes": [
        {"id": "1", "left": 3, "right": 2, "value": 1},
        {"id": "2", "left": None, "right": 4, "value": 2},
        {"id": "3", "left": 5, "right": None, "value": 3},
        {"id": "3", "left": 7, "right": None, "value": 5},
        {"id": "3", "left": None, "right": 6, "value": 4}

    ],
    "root": 1
}
print(MaximumWidth(data).MaximumWidth())