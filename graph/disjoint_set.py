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

'''


class DisjointedSet:

    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]

    def union(self, v1, v2):
        v1_parent = self.get_parent(v1)
        v2_parent = self.get_parent(v2)
        if v1_parent != v2_parent:
            if self.rank[v1_parent] == self.rank[v2_parent]:
                self.parent[v2_parent] = v1_parent
                self.rank[v1_parent] += 1
            elif self.rank[v1_parent] > self.rank[v2_parent]:
                self.parent[v2_parent] = v1_parent
            else:
                self.parent[v1_parent] = v2_parent

    def get_parent(self, v):
        current = v
        while current != self.parent[current]:
            current = self.parent[current]
        self.parent[v] = current
        return current


d = DisjointedSet(7)
print(d.get_parent(1))
print(d.get_parent(2))
print(d.union(1, 2))
print(d.union(2, 3))
print(d.union(4, 5))
print(d.union(6, 7))
print(d.union(5, 6))
print(d.union(3, 7))
print(d.get_parent(1))
print(d.get_parent(2))
print(d.get_parent(3))
print(d.get_parent(4))
print(d.get_parent(5))
print(d.get_parent(6))
print(d.get_parent(7))
