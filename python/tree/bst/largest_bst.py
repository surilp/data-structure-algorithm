from tree.Tree import Tree


class LargestBST(Tree):

    def __init__(self, data):
        super().__init__(data)

    def largest_bst(self):
        return self._largest_bst(self.root)

    def _largest_bst(self, node):

        if node:
            if node.left:
                l_smallest, l_largest, l_count, l_result = self._largest_bst(node.left)
            else:
                l_smallest, l_largest, l_count, l_result = node.val, node.val, 0, 0
            if node.right:
                r_smallest, r_largest, r_count, r_result = self._largest_bst(node.right)
            else:
                r_smallest, r_largest, r_count, r_result = node.val, node.val, 0,0

            if l_largest <= node.val <= r_smallest:
                count = l_count + r_count + 1
                return l_smallest, r_largest, count, max(count, l_result, r_result)
            else:
                return float('inf'), float('inf'), 0, max(l_result, r_result)


data = [20, 15, 40, 14, 18, 30, 60, None, 17, 16, 19, None, None, 50]
t = LargestBST(data)
print(t.largest_bst())
