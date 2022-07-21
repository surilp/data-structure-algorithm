from tree.Tree import Tree


class FlattenTree(Tree):

    def __init__(self, data):
        super(FlattenTree, self).__init__(data)

    def flatten_tree_rec(self):
        prev = [None]
        self._flatten_tree_rec(self.root, prev)

    def _flatten_tree_rec(self, node, prev):
        if node:
            self._flatten_tree_rec(node.right, prev)
            self._flatten_tree_rec(node.left, prev)

            node.right = prev[0]
            node.left = None
            prev[0] = node

    def traveral(self):
        result = []
        current = self.root
        while current:
            result.append(current.val)
            current = current.right
        return result

    def flatten_stack(self):
        stack = [self.root]
        while stack:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            current.right = stack[-1] if stack else None
            current.left = None

    def flatten_morris_traversal(self):
        current = self.root

        while current:
            if current.left:
                prev = current.left
                while prev.right:
                    prev = prev.right
                prev.right = current.right
                current.right = current.left
                current.left = None
            current = current.right


data = [1, 2, 5, 3, 4, None, 6, None, None, None, None, None, None, 7, None]
t = FlattenTree(data)
print(t.flatten_tree_rec())
print(t.traveral())

data = [1, 2, 5, 3, 4, None, 6, None, None, None, None, None, None, 7, None]
t = FlattenTree(data)
print(t.flatten_stack())
print(t.traveral())

data = [1, 2, 5, 3, 4, None, 6, None, None, None, None, None, None, 7, None]
t = FlattenTree(data)
print(t.flatten_morris_traversal())
print(t.traveral())
