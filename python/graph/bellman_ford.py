'''
shortest path with negative weight

directed graph - if there is negative cycle it will not work
undirected graph - convert it to directed graph

1) relax all edges for n-1
distnace array = start with any vertex everything else inf
distance[source] + u to v < distance[v]
'''


def bellman_ford(n, edges):
    distance = [float('inf')] * n
    distance[0] = 0
    for _ in range(n):
        for from_v, to_v, weight in edges:
            if distance[from_v] + weight < distance[to_v]:
                distance[to_v] = distance[from_v] + weight

    for from_v, to_v, weight in edges:
        if distance[from_v] + weight < distance[to_v]:
            return None
            distance[to_v] = distance[from_v] + weight
    return distance


n = 6
edges = [
    [0, 1, 5],
    [1, 5, -3],
    [5, 3, 1],
    [3, 2, 6],
    [1, 2, -2],
    [2, 4, 3],
    [3, 4, -2]
]
print(bellman_ford(n, edges))

n = 6
edges = [
    [0, 1, 5],
    [1, 5, -3],
    [5, 3, 1],
    [3, 2, 6],
    [1, 2, -2],
    [2, 4, 3],
    [4, 3, -10]
]
print(bellman_ford(n, edges))
