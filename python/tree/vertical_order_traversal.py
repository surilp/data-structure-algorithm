'''

'''

from tree.Tree import Tree
from heapq import heappop, heappush
from collections import OrderedDict
from pprint import pprint


class VerticalTraversal(Tree):

    def __init__(self, data):
        super().__init__(data)

    def vertical_traversal(self):
        order_map = OrderedDict()
        self._vertical_traversal(self.root, order_map, 0, 0)
        pprint(order_map)

    def _vertical_traversal(self, node, order_map, x, y):
        if node:
            self._vertical_traversal(node.left, order_map, x - 1, y + 1)
            if x not in order_map:
                order_map[x] = {y: []}
            elif y not in order_map[x]:
                order_map[x][y] = []
            order_map[x][y].append(node.val)
            self._vertical_traversal(node.right, order_map, x + 1, y + 1)


data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 10, "value": 2},
        {"id": "2", "left": 9, "right": 10, "value": 3},
        {"id": "2", "left": None, "right": 5, "value": 4},
        {"id": "2", "left": None, "right": 6, "value": 5}
    ],
    "root": 1
}

print(VerticalTraversal(data).vertical_traversal())
