from tree.Tree import Tree

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2}
    ],
    "root": 1
}

data2 = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 6, "value": 3},
        {"id": "2", "left": 5, "right": None, "value": 4},
        {"id": "2", "left": 9, "right": None, "value": 5},
        {"id": "2", "left": None, "right": 7, "value": 6},
        {"id": "2", "left": None, "right": 8, "value": 7},
    ],
    "root": 1
}

'''
longest path between any two node
does not need to pass via root
'''


class BinaryTreeDiameter(Tree):

    def __init__(self, data):
        super().__init__(data)

    def get_diameter(self):
        return self._get_diameter(self.root)[1]

    def _get_diameter(self, node):
        if node:
            left, l_dia = self._get_diameter(node.left)
            right, r_dia = self._get_diameter(node.right)
            return 1 + max(left, right), max(l_dia, r_dia, left + right)
        else:
            return 0, 0


print(BinaryTreeDiameter(data).get_diameter())
print(BinaryTreeDiameter(data2).get_diameter())
