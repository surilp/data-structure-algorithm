from tree.Tree import Tree


class KthSmallest(Tree):

    def __init__(self, data):
        super(KthSmallest, self).__init__(data)

    def kth_smallest(self, k):
        node = self.root
        return self._kth_smallest(node, [0], k)

    def _kth_smallest(self, node, counter, k):
        if node:
            left = self._kth_smallest(node.left, counter, k)
            if left is not None:
                return left
            counter[0] += 1
            if counter[0] == k:
                return node.val
            return self._kth_smallest(node.right, counter, k)


data = [5, 3, 7, 1, 4, 6, 8, None, 2]
print(KthSmallest(data).kth_smallest(4))
