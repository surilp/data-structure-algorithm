from tree.Tree import Tree
from collections import deque

class RootToNodePath(Tree):

    def __init__(self, data):
        super().__init__(data)

    def path(self, node):
        result = deque()
        self._path_v2(self.root, node, result)
        return result


    def _path(self, node, target, result):
        if node:
            if self._path(node.left, target, result):
                result.appendleft(node.val)
                return True
            if self._path(node.right, target, result):
                result.appendleft(node.val)
                return True
            if node.val == target:
                result.appendleft(node.val)
                return True

    def _path_v2(self, node, target, result):
        if node:
            result.append(node.val)
            if node.val == target:
                return True
            left = self._path_v2(node.left, target, result)
            right = self._path_v2(node.right, target, result)
            if not right and not left:
                result.pop()
            return left or right
        else:
            return False

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "3", "left": 6, "right": 7, "value": 5}
    ],
    "root": 1
}
print(RootToNodePath(data).path(6))