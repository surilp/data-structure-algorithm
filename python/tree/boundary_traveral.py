'''
left boundary
leaves
right boundary reverse
'''


from tree.Tree import Tree


class BondaryTraversal(Tree):

    def __init__(self, data):
        super().__init__(data)

    def boundary_traversal(self):
        result = []
        self._boundary_traversal(self.root, result)
        return result

    def _boundary_traversal(self, node, result):
        cur = node
        parent = None
        while cur and (cur.left or cur.right):
            result.append(cur.val)
            parent = cur
            cur = cur.left
            if not cur:
                cur = parent.right
        if parent and parent.left:
            result.append(parent.left.val)
        if parent and parent.right:
            result.append(parent.right.val)
        cur = node.right
        self._right_boundary(cur, result)

        return result
    def _right_boundary(self, node, result):
        if (node.right and (node.right.left is None and node.right.right is None)) or \
                (node.left and (node.left.left is None and node.left.right is None)):
            if node.left:
                result.append(node.left.val)
            if node.right:
                result.append(node.right.val)
            result.append(node.val)
            return
        if node.right:
            self._right_boundary(node.right, result)
            result.append(node.val)
        elif node.left:
            self._right_boundary(node.left, result)
            result.append(node.val)


data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 7, "value": 1},
        {"id": "2", "left": 3, "right": None, "value": 2},
        {"id": "2", "left": None, "right": 4, "value": 3},
        {"id": "2", "left": 5, "right": 6, "value": 4},
        {"id": "2", "left": None, "right": 8, "value": 7},
        {"id": "2", "left": 9, "right": None, "value": 8},
        {"id": "2", "left": 10, "right": 11, "value": 9},
    ],
    "root": 1
}

print(BondaryTraversal(data).boundary_traversal())