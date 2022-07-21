from tree.Tree import Tree, Node

data = [3, 1, 4, None, None, 2, None]

t = Tree(data)


class Solution:
    def recoverTree(self, root) -> None:
        prev = Node(-float('inf'))
        first = None
        mid = None
        last = None

        def helper(node):
            nonlocal prev
            nonlocal first
            nonlocal mid
            nonlocal last

            if node:
                helper(node.left)
                if node.val < prev.val:
                    if not first:
                        first = prev
                        mid = node
                    else:
                        last = node
                prev = node
                helper(node.right)

        helper(root)
        if last:
            first.val, last.val = last.val, first.val
        else:
            first.val, mid.val = mid.val, first.val


Solution().recoverTree(t.root)
pass
