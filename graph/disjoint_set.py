'''
kruskal algo

if two node belong to same componenet or no

findparent - parent of the component
union - combine two into 1 componenet

1) array  each node parent of themselves
2) rank array - initially all will be 0

1) union(1,2)
    - check if parent are differnt
    - if different = attache 2 to 1 or 1 to 2
    - if 2 to 1 is attached, then rank of 1 increment

# if two nodes belong to same component
# union - initially self is root, when you connect two one become parent of another, connect root of two parent
# find parent
# path compression
# smaller size to bigger size component

'''


class DSU:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def union(self, u, v):
        u_parent = self.find_parent(u)
        v_parent = self.find_parent(v)

        if u_parent != v_parent:
            if self.size[u_parent] < self.size[v_parent]:
                self.parent[u_parent] = v_parent
                self.size[v_parent] += self.size[u_parent]
            else:
                self.parent[v_parent] = u_parent
                self.size[u_parent] += self.size[v_parent]

    def find_parent(self, node):
        temp = node
        while self.parent[temp] != temp:
            temp = self.parent[temp]
        self.parent[node] = temp
        return self.parent[node]
