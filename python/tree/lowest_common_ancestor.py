from tree.Tree import Tree


class LowerCommonAncestor(Tree):

    def __init__(self, data):
        super().__init__(data)

    def lowest_common_ancestor(self, node1_val, node2_val):
        return self._lowest_common_ancestor(self.root, node1_val, node2_val)

    def _lowest_common_ancestor(self, node, target1, target2):
        if node:
            left = self._lowest_common_ancestor(node.left, target1, target2)
            right = self._lowest_common_ancestor(node.right, target1, target2)

            if node.val in [target1, target2] or (left and right):
                return node.val
            if left:
                return left
            if right:
                return right


data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "3", "left": 8, "right": 9, "value": 3},
        {"id": "3", "left": 6, "right": 7, "value": 5}
    ],
    "root": 1
}
print(LowerCommonAncestor(data).lowest_common_ancestor(2, 3))