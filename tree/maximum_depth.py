from tree.Tree import Tree

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": None, "right": None, "value": 2},
        {"id": "3", "left": 4, "right": 6, "value": 3},
        {"id": "4", "left": 5, "right": None, "value": 4}
    ],
    "root": 1
}


class MaxDepth(Tree):

    def __init__(self, data):
        super().__init__(data)

    def max_depth_dfs(self):
        return self._max_depth_dfs(self.root)

    def max_depth_bfs(self):
        return self._max_depth_bfs(self.root)

    def _max_depth_dfs(self, node):
        if node:
            left = self._max_depth_dfs(node.left)
            right = self._max_depth_dfs(node.right)
            return 1 + max(left, right)
        else:
            return 0

    def _max_depth_bfs(self, node):
        from collections import deque
        queue = deque()
        queue.append(node)
        level = 0
        while queue:
            size = len(queue)
            level += 1
            while size > 0:
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                size -= 1
        return level


max_depth = MaxDepth(data)
print(max_depth.max_depth_dfs())
print(max_depth.max_depth_bfs())
