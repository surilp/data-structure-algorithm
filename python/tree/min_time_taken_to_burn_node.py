from tree.Tree import Tree
from collections import deque


class BurnNode(Tree):

    def __init__(self, data):
        super().__init__(data)

    def burn(self, target):
        target_node = self.find_node(target)
        parent_pointers = self.get_parent_pointers(self.root)
        visited = set()
        queue = deque()
        queue.append(target_node)
        visited.add(target_node)
        step = -1
        while queue:
            size = len(queue)
            while size > 0:
                current = queue.popleft()
                if current.left and current.left not in visited:
                    visited.add(current.left)
                    queue.append(current.left)
                if current.right and current.right not in visited:
                    visited.add(current.right)
                    queue.append(current.right)
                if current in parent_pointers and parent_pointers[current] and parent_pointers[current] not in visited:
                    visited.add(parent_pointers[current])
                    queue.append(parent_pointers[current])
                size -= 1
            step += 1
        return step

    def find_node(self, target):
        return self._find_node(self.root, target)

    def _find_node(self, node, target):
        if node:
            if node.val == target:
                return node
            left = self._find_node(node.left, target)
            if left:
                return left
            right = self._find_node(node.right, target)
            return right


data = [1, 2, 3, 4, None, 5, 6, None, 7]
tree = BurnNode(data)
print(tree.burn(2))

data = [1, 2, 3, 4, None, 5, 6, None, 7]
tree = BurnNode(data)
print(tree.burn(2))