'''
first do topo sort

'''


n = 6
edges = [
    [0, [1, 2]],
    [0, [4, 1]],
    [1, [2, 3]],
    [2, [3, 6]],
    [4, [2, 2]],
    [4, [5, 4]],
    [5, [3, 1]]
]


def _get_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]
    for from_v, to_v in edges:
        adj_list[from_v].append(to_v)
    return adj_list

def shortest_path_DAG(n, edges, source):
    adj_list = _get_adj_list(n, edges)
    topo_result = topo_sort(n, edges)
    distance = [float('inf')] * n
    distance[source] = 0

    while topo_result:
        current = topo_result.pop()
        if distance[current] < float('inf'):
            for adj_vertex, weight in adj_list[current]:
                if distance[adj_vertex] > distance[current] + weight:
                    distance[adj_vertex] = distance[current] + weight
    return distance


def topo_sort(n, edges):
    adj_list = _get_adj_list(n, edges)
    visited = [None] * n
    result = []
    for vertex in range(n):
        if not visited[vertex]:
            _topo_sort(adj_list, visited, result, vertex)
    return result

def _topo_sort(adj_list, visited, result, vertex):
    visited[vertex] = True
    for adj_vertex, _ in adj_list[vertex]:
        if not visited[adj_vertex]:
            _topo_sort(adj_list, visited, result, adj_vertex)
    result.append(vertex)

print(topo_sort(n, edges))

print(shortest_path_DAG(n, edges, 0))
