def convert_to_linked_list(root):
    left, right = helper(root)
    return left, right


def helper(node):
    if node:

        l_l, l_r = helper(node.left)
        r_l, r_r = helper(node.right)

        if l_r:
            l_r.right = node
        if r_l:
            r_l.left = node

        node.left = l_r
        node.right = r_l

        if not l_l:
            l_l = node
        if not r_r:
            r_r = node
        return l_l, r_r
    else:
        return None, None

def traversal(node, forward= True):
    if forward:
        while node:
            print(node.val)
            node = node.right
    else:
        while node:
            print(node.val)
            node = node.left



from tree.Tree import Tree

data = [100, 50, 200, 25, 75, 125, 350,None, 30, 60]

t = Tree(data)
head, tail = convert_to_linked_list(t.root)
traversal(head)
traversal(tail, forward=False)
