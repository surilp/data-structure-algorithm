from tree.Tree import Node


class BinaryTree:

    def __init__(self, inorder, preorder):
        self.root = Node(preorder[0])
        i = inorder.index(preorder[0])
        self.build(self.root, inorder[:i], preorder[1: i + 1], True)
        self.build(self.root, inorder[i + 1:], preorder[i + 1:], False)
        pass

    def build(self, node, inorder, preorder, is_left):
        if inorder:
            if is_left:
                node.left = Node(preorder[0])
                node = node.left
            else:
                node.right = Node(preorder[0])
                node = node.right

            i = inorder.index(preorder[0])
            self.build(node, inorder[:i], preorder[1: i + 1], True)
            self.build(node, inorder[i + 1:], preorder[i + 1:], False)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


in_order = [40, 20, 50, 10, 60, 30]
pre_order = [10, 20, 40, 50, 30, 60]

tree = BinaryTree(in_order, pre_order)

print(tree.preorder())
assert tree.preorder() == pre_order

print(tree.inorder())
assert tree.inorder() == in_order
