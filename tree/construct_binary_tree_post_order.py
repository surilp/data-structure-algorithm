from tree.Tree import Node


class BinaryTree:

    def __init__(self, inorder, postorder):
        n = len(inorder)
        inorder_map = {num: i for i, num in enumerate(inorder)}
        self.root = self._build(inorder, postorder, inorder_map, 0, n - 1, 0, n - 1)
        pass

    def _build(self, inorder, postorder, inorder_map, in_start, in_end, post_start, post_end):
        if in_start > in_end:
            return None
        node = Node(postorder[post_end])
        i = inorder_map[postorder[post_end]]
        right_size = in_end - (i + 1)
        node.left = self._build(inorder, postorder, inorder_map, in_start, i - 1, post_start,
                                post_end - 1 - right_size - 1)
        node.right = self._build(inorder, postorder, inorder_map, i + 1, in_end, post_end - 1 - right_size,
                                 post_end - 1)
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)


in_order = [40, 20, 50, 10, 60, 30]
post_order = [40, 50, 20, 60, 30, 10]

b = BinaryTree(in_order, post_order)
print(b.inorder())
print(b.postorder())
