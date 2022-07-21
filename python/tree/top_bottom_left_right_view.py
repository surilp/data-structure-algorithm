from tree.Tree import Tree
from collections import deque


class TopBottomLeftRightView(Tree):

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

    def left_view(self):
        queue = deque()
        queue.append(self.root)
        result = []
        while queue:
            size = len(queue)
            max_size = size
            while size > 0:
                current = queue.popleft()
                if size == max_size:
                    result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                size -= 1
        return result

    def right_view(self):
        queue = deque()
        queue.append(self.root)
        result = []
        while queue:
            size = len(queue)
            while size > 0:
                current = queue.popleft()
                if size == 1:
                    result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                size -= 1
        return result

    def right_view_recursive(self):
        result = []
        self._right_view_recursive(self.root, result, 0)
        return result

    def _right_view_recursive(self, node, result, current_level):
        if node:
            if current_level == len(result):
                result.append(node.val)
            self._right_view_recursive(node.right, result, current_level + 1)
            self._right_view_recursive(node.left, result, current_level + 1)

    def left_view_recursive(self):
        result = []
        self._left_view_recursive(self.root, result, 0)
        return result

    def _left_view_recursive(self, node, result, current_level):
        if node:
            if current_level == len(result):
                result.append(node.val)
            self._left_view_recursive(node.left, result, current_level + 1)
            self._left_view_recursive(node.right, result, current_level + 1)


data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "2", "left": None, "right": 7, "value": 3},
        {"id": "2", "left": 6, "right": None, "value": 5}
    ],
    "root": 1
}
print(TopBottomLeftRightView(data).top_view())

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "2", "left": 6, "right": 7, "value": 3},
        {"id": "2", "left": 8, "right": 9, "value": 5}
    ],
    "root": 1
}
print(TopBottomLeftRightView(data).bottom_view())

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "2", "left": None, "right": 7, "value": 3},
        {"id": "2", "left": 6, "right": None, "value": 5}
    ],
    "root": 1
}
print(TopBottomLeftRightView(data).right_view())
print(TopBottomLeftRightView(data).right_view_recursive())
print(TopBottomLeftRightView(data).left_view())
print(TopBottomLeftRightView(data).left_view_recursive())
