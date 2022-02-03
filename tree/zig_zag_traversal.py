from tree.Tree import Tree


class ZigZag(Tree):

    def __init__(self, data):
        super().__init__(data)

    def zig_zag_traversal(self):
        result = []
        self._zig_zag_traversal(self.root, result)
        return result

    def _zig_zag_traversal(self, node, result):
        from collections import deque
        queue = deque()
        queue.append(node)
        reverse = False
        while queue:
            size = len(queue)
            temp = []
            reverse = not reverse
            while size > 0:
                current = queue.pop() if reverse else queue.popleft()
                temp.append(current.val)
                if reverse:
                    if current.right:
                        queue.appendleft(current.right)
                    if current.left:
                        queue.appendleft(current.left)
                else:
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                size -= 1
            result.append(temp)
        return result

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "2", "left": None, "right": 6, "value": 3}
    ],
    "root": 1
}

print(ZigZag(data).zig_zag_traversal())