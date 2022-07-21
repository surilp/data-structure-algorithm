from tree.Tree import Tree


class SameTree(Tree):

    def __init__(self, data):
        super().__init__(data)

    def __eq__(self, other):
        return self._if_two_tree_equal(self.root, other.root)

    def _if_two_tree_equal(self, node1, node2):
        if not node1 and not node2:
            return True
        if (node1 and not node2) or (node2 and not node1):
            return False
        if node1.val == node2.val:
            if not self._if_two_tree_equal(node1.left, node2.left):
                return False
            return self._if_two_tree_equal(node1.right, node2.right)
        else:
            return False


data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 3}
    ],
    "root": 1
}

data2 = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 3}
    ],
    "root": 1
}

tree1 = SameTree(data)
tree2 = SameTree(data2)

print(tree1 == tree2)
