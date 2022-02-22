'''
{
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "3", "left": 6, "right": 7, "value": 3},
        {"id": "4", "left": 8, "right": 9, "value": 4},
        {"id": "5", "left": None, "right": None, "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": None, "right": None, "value": 7},
        {"id": "8", "left": None, "right": None, "value": 8},
        {"id": "9", "left": None, "right": None, "value": 9}
    ],
    "root": 1
}
'''
from collections import deque


class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash((self.val, self.left, self.right))


class Tree:

    def __init__(self, data):
        if isinstance(data, dict):
            self.root = Node(data["root"])
            self.insert_nodes(data["nodes"])
        elif isinstance(data, list):
            self.root = self.insert_nodes_from_arr(data)
            pass

    def insert_nodes_from_arr(self, data):
        data_len = len(data)
        for idx in range(data_len):
            if data[idx]:
                data[idx] = Node(data[idx])
        for idx in range(data_len):
            current = data[idx]
            if current:
                right = self.get_right_child_idx(idx, data_len)
                left = self.get_left_child_idx(idx, data_len)
                if left:
                    current.left = data[left]
                if right:
                    current.right = data[right]
        return data[0]

    def get_right_child_idx(self, parent, n):
        right = (2 * parent) + 2
        return right if right < n else None

    def get_left_child_idx(self, parent, n):
        left = (2 * parent) + 1
        return left if left < n else None

    def insert_nodes(self, nodes):
        node_map = {self.root.val: self.root}
        for node in nodes:
            val = node["value"]
            left = node["left"]
            right = node["right"]
            if val not in node_map:
                node_map[val] = Node(val)
            if left and left not in node_map:
                node_map[left] = Node(left)
            if right and right not in node_map:
                node_map[right] = Node(right)
            node_map[val].left = node_map[left] if left else None
            node_map[val].right = node_map[right] if right else None

    # DFS
    def pre_order_traversal(self):
        return self.traversal(self._pre_order_traversal)

    def in_order_traversal(self):
        return self.traversal(self._in_order_traversal)

    def post_order_traversal(self):
        return self.traversal(self._post_order_traversal)

    def traversal(self, func):
        node = self.root
        result = []
        func(node, result)
        return result

    def _pre_order_traversal(self, node, result):
        if node:
            result.append(node.val)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.val)
            self._in_order_traversal(node.right, result)

    def _post_order_traversal(self, node, result):
        if node:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.val)

    def level_order(self):
        queue = deque()
        queue.append(self.root)
        result = []
        while queue:
            current = queue.popleft()
            result.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def level_order_v2(self):
        queue = deque()
        queue.append(self.root)
        result = []
        while queue:
            size = len(queue)
            temp = []
            while size > 0:
                current = queue.popleft()
                temp.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                size -= 1
            result.append(temp)
        return result

    def iterative_pre_order_traversal(self):
        stack = [self.root]
        result = []
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

    def iterative_in_order_traversal(self):
        stack = []
        result = []
        node = self.root
        self._iterative_add_to_stack(stack, node)
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                self._iterative_add_to_stack(stack, current.right)
        return result

    def _iterative_add_to_stack(self, stack, node):
        while node:
            stack.append(node)
            node = node.left

    def iterative_post_order_traversal_2_stacks(self):
        stack1 = [self.root]
        stack2 = []
        result = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            result.append(stack2.pop().val)
        return result

    def iterative_post_order_traversal_1_stacks(self):
        stack = []
        result = []
        cur = self.root

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack[-1]
                cur = cur.right
                if not cur:
                    temp = stack.pop()
                    result.append(temp.val)
                    while stack and stack[-1].right and stack[-1].right == temp:
                        temp = stack.pop()
                        result.append(temp.val)
                    cur = None
        return result

    def all_dfs_traversal(self):
        stack = [[self.root, 1]]
        pre_order = []
        in_order = []
        post_order = []
        while stack:
            current, order = stack[-1]
            if order == 1:
                pre_order.append(current.val)
                stack[-1][1] += 1
                if current.left:
                    stack.append([current.left, 1])
            elif order == 2:
                in_order.append(current.val)
                stack[-1][1] += 1
                if current.right:
                    stack.append([current.right, 1])
            elif order == 3:
                post_order.append(current.val)
                stack.pop()
        return pre_order, in_order, post_order

    def get_parent_pointers(self, node):
        queue = deque()
        queue.append(node)
        parent_pointer = {}
        while queue:
            current = queue.popleft()
            if current.left:
                parent_pointer[current.left] = current
                queue.append(current.left)
            if current.right:
                parent_pointer[current.right] = current
                queue.append(current.right)
        return parent_pointer