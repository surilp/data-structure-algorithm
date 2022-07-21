from tree.Tree import Tree

class MorrisTraveral(Tree):

    def __init__(self, data):
        super(MorrisTraveral, self).__init__(data)

    def morris_traversal_inorder(self):
        result = []
        current = self.root
        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right

                if prev.right:
                    prev.right = None
                    result.append(current.val)
                    current = current.right
                else:
                    prev.right = current
                    current = current.left
        return result

    def morris_traversal_preorder(self):
        result = []
        current = self.root
        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                prev = current.left
                while prev.right and prev.right != current:
                    prev = prev.right

                if prev.right:
                    prev.right = None
                    current = current.right
                else:
                    prev.right = current
                    result.append(current.val)
                    current = current.left
        return result



data = [1, 2, 3, 4, 5, None, None, None, None, None, 6]
tree = MorrisTraveral(data)
print(tree.in_order_traversal())
print(tree.morris_traversal_inorder())
print(tree.pre_order_traversal())
print(tree.morris_traversal_preorder())