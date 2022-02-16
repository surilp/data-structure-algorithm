'''
parent pointers
'''

from tree.Tree import Tree


class NodeAtDistanceK(Tree):

    def __init__(self, data):
        super().__init__(data)

    def nodes_at_distance_k(self, k, target):
        result = []
        parent_pointers = self.get_parent_pointers(self.root)
        self._nodes_at_distance_k(self.root, k, target, result, False)
        return result

    def _nodes_at_distance_k(self, node, k, target, result, flag):
        if node:
            if k == 0:
                result.append(node.val)
                return

            if node.val == target or flag:
                if not flag:
                    flag = True
                self._nodes_at_distance_k(node.left, k - 1, target, result, flag)
                self._nodes_at_distance_k(node.right, k - 1, target, result, flag)
            else:
                self._nodes_at_distance_k(node.left, k, target, result, flag)
                self._nodes_at_distance_k(node.right, k, target, result, flag)


data = {
    "nodes": [
        {"id": "1", "left": 5, "right": 1, "value": 3},
        {"id": "2", "left": 6, "right": 2, "value": 5},
        {"id": "3", "left": 0, "right": 8, "value": 1},
        {"id": "3", "left": 7, "right": 4, "value": 2},
    ],
    "root": 3
}

tree = NodeAtDistanceK(data)
print(tree.nodes_at_distance_k(2, 5))
