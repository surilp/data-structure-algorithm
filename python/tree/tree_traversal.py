from tree.Tree import Tree

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "3", "left": 7, "right": 8, "value": 3},
        {"id": "4", "left": None, "right": None, "value": 4},
        {"id": "5", "left": 6, "right": None, "value": 5},
        {"id": "6", "left": None, "right": None, "value": 6},
        {"id": "7", "left": None, "right": None, "value": 7},
        {"id": "8", "left": 9, "right": 10, "value": 8},
        {"id": "9", "left": None, "right": None, "value": 9},
        {"id": "10", "left": None, "right": None, "value": 10},
    ],
    "root": 1
}

tree = Tree(data)
print(f'recursive pre order = {tree.pre_order_traversal()}')
print(f'iterative pre order = {tree.iterative_pre_order_traversal()}')
print(f'recursive in order = {tree.in_order_traversal()}')
print(f'iterative in order = {tree.iterative_in_order_traversal()}')
print(f'recursive post order = {tree.post_order_traversal()}')
print(f'iterative post order 2  = {tree.iterative_post_order_traversal_2_stacks()}')
print(f'iterative post order 1= {tree.iterative_post_order_traversal_2_stacks()}')
for order in tree.all_dfs_traversal():
    print(order)

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 3, "value": 1},
        {"id": "2", "left": 4, "right": 5, "value": 2},
        {"id": "3", "left": 6, "right": 7, "value": 3}
    ],
    "root": 1
}
tree = Tree(data)

print(tree.level_order())
print(tree.level_order_v2())

data = {
    "nodes": [
        {"id": "1", "left": 2, "right": 7, "value": 1},
        {"id": "2", "left": 3, "right": None, "value": 2},
        {"id": "3", "left": 8, "right": 9, "value": 7},
        {"id": "3", "left": None, "right": 10, "value": 9},
        {"id": "3", "left": None, "right": 4, "value": 3},
        {"id": "3", "left": None, "right": 5, "value": 4},
        {"id": "3", "left": None, "right": 6, "value": 5},
        {"id": "3", "left": None, "right": None, "value": 6},

    ],
    "root": 1
}
tree = Tree(data)

print(tree.iterative_post_order_traversal_1_stacks())

for order in tree.all_dfs_traversal():
    print(order)
