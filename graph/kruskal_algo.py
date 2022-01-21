'''
no adj list needed

(1) sort all the edges according to weight (weight, u, v)
(2) pick shortest weight and check u and v are from same component
(3) if not take the that edge

T - E Log E
S - E
'''

from dataclasses import dataclass, field
from typing import List


@dataclass
class Edge:
    weight: int
    parent: int
    child: int

    def __lt__(self, other):
        return self.weight < other.weight


@dataclass
class Vertex:
    parent: int = None
    children: List[Edge] = field(default_factory=list)


class DisJointedSet:

    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [idx for idx in range(n + 1)]

    def get_parent(self, vertex):
        if vertex == self.parent[vertex]:
            return vertex
        p = self.get_parent(self.parent[vertex])
        self.parent[vertex] = p
        return p

    def union(self, v1, v2):
        v1 = self.get_parent(v1)
        v2 = self.get_parent(v2)

        if self.rank[v1] > self.rank[v2]:
            self.parent[v2] = v1
        elif self.rank[v1] < self.rank[v2]:
            self.parent[v1] = v2
        else:
            self.parent[v2] = v1
            self.rank[v1] += 1

    def from_same_component(self, v1, v2):
        return self.get_parent(v1) == self.get_parent(v2)


def kruskal_algo(edges, n):
    edges.sort()
    disjointed_set = DisJointedSet(n)
    result = 0
    for edge in edges:
        if not disjointed_set.from_same_component(edge.parent, edge.child):
            disjointed_set.union(edge.parent, edge.child)
            result += edge.weight
    return result


edges = [
    Edge(9, 5, 4),
    Edge(4, 5, 1),
    Edge(1, 4, 1),
    Edge(5, 4, 3),
    Edge(2, 1, 2),
    Edge(3, 4, 2),
    Edge(3, 2, 3),
    Edge(8, 3, 6),
    Edge(7, 2, 6)
]

n = 6

print(kruskal_algo(edges, 6))
