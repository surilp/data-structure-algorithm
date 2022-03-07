'''
convert it into tree such that in that tree you can reach any node
number of nodes = n
number of edges = n - 1
minimum cost

kruskals parent
1) sort edges according to weight to weight
2) if ultimate parent not same union
'''

from graph.Graph import Graph
from collections import namedtuple
from typing import List
from disjoint_set import DSU

Node = namedtuple('Node', ['u', 'v', 'w'])


def kruskal(n: int, edges: List[Node]) -> int:
    edges.sort(key=lambda x: x.w)
    dsu = DSU(n)
    cost = 0
    for edge in edges:
        if dsu.find_parent(edge.u) != dsu.find_parent(edge.v):
            dsu.union(edge.u, edge.v)
            cost += edge.w
    return cost




edges = [
    Node(5, 0, 9),
    Node(5, 1, 4),
    Node(1, 0, 1),
    Node(1, 2, 3),
    Node(1, 3, 2),
    Node(0, 2, 5),
    Node(2, 3, 3),
    Node(2, 4, 8),
    Node(3, 4, 7)
]

n = 6

print(kruskal(n, edges))
