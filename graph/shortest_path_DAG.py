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
    distance = [float('inf')] * n
    distance[source] = 0
    _dfs(adj_list, distance, source)
    return distance

def _dfs(adj_list, distance, source):
    for adj_vertex, weight in adj_list[source]:
        if distance[adj_vertex] > distance[source] + weight:
            distance[adj_vertex] = distance[source] + weight
            _dfs(adj_list, distance, adj_vertex)


print(shortest_path_DAG(n, edges, 0))