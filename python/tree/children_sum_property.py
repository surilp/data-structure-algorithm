from tree.Tree import Tree


class ChildrenSumPreperty(Tree):

    def __init__(self, data):
        super().__init__(data)

    def children_sum_property(self):
        return self._children_sum_property(self.root)

    def _children_sum_property(self, node):
        if node:
            left_val = node.left.val if node.left else 0
            right_val = node.right.val if node.right else 0
            total = left_val + right_val
            if node.val > total:
                if node.left:
                    node.left.val = node.val
                if node.right:
                    node.right.val = node.val
            else:
                node.val = total
            left = self._children_sum_property(node.left)
            right = self._children_sum_property(node.right)
            if left and right:
                node.val = left.val + right.val
            elif left:
                left.val = node.val
            elif right:
                right.val = node.val
            return node


data = {
    "nodes": [
        {"id": "1", "left": 10, "right": 20, "value": 40},
        {"id": "2", "left": 2, "right": 5, "value": 10},
        {"id": "3", "left": 30, "right": 50, "value": 20}
    ],
    "root": 40
}

tree = ChildrenSumPreperty(data)
print(tree.iterative_in_order_traversal())
print(tree.children_sum_property())
print(tree.iterative_in_order_traversal())
