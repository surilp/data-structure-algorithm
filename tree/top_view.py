from tree.Tree import Tree
from collections import deque


class TopView(Tree):

    def __init__(self, data):
        super().__init__(data)

    def top_view(self):
        result_map = {}
        queue = deque()
        queue.append((0, self.root))

        while queue:
            current_x, c_node = queue.popleft()
            if current_x not in result_map:
                result_map[current_x] = c_node.val
            if c_node.left:
                queue.append((current_x - 1, c_node.left))
            if c_node.right:
                queue.append((current_x + 1, c_node.right))
        result_list = sorted(list(result_map.items()))
        return [num for _, num in result_list]

    def bottom_view(self):
        result_map = {}
        queue = deque()
        queue.append((0, self.root))

        while queue:
            current_x, c_node = queue.popleft()
            result_map[current_x] = c_node.val
            if c_node.left:
                queue.append((current_x - 1, c_node.left))
            if c_node.right:
                queue.append((current_x + 1, c_node.right))
        result_list = sorted(list(result_map.items()))
        return [num for _, num in result_list]


data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "2", "left": None, "right": 7, "value": 3},
        {"id": "2", "left": 6, "right": None, "value": 5}
    ],
    "root": 1
}

print(TopView(data).top_view())

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "2", "left": 6, "right": 7, "value": 3},
        {"id": "2", "left": 8, "right": 9, "value": 5}
    ],
    "root": 1
}

print(TopView(data).bottom_view())
