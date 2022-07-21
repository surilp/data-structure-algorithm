from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class Tree:
    def __init__(self, data):
        self.root = self.deserialize(data)

    def deserialize(self, data):
        if not data:
            return None
        queue = deque()
        root = Node(data[0])
        n = len(data)
        queue.append(root)
        idx = 1
        while queue and idx < n:
            current = queue.popleft()
            if idx < n:
                if data[idx] is not None:
                    node = Node(data[idx])
                else:
                    node = None
                current.left = node
                queue.append(node)
                idx += 1
            if idx < n:
                if data[idx] is not None:
                    node = Node(data[idx])
                else:
                    node = None
                current.right = node
                queue.append(node)
                idx += 1
        return root

    def serialize(self):
        result = []
        queue = deque()
        queue.append(self.root)
        while queue:
            current = queue.popleft()
            if current:
                result.append(current.value)
            else:
                result.append(None)
                continue
            if current.left:
                queue.append(current.left)
            else:
                queue.append(None)
            if current.right:
                queue.append(current.right)
            else:
                queue.append(None)
        return result

    def pre_order_dfs_recursion(self):
        result = []
        def helper(node):
            if node:
                result.append(node.value)
                helper(node.left)
                helper(node.right)
        helper(self.root)
        return result
