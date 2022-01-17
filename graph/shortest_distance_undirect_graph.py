from collections import deque

n = 9
edges = [[0, 1], [0, 3], [1, 2], [1, 3], [3, 4], [4, 5], [5, 6], [2, 6], [6, 7], [6, 8], [7, 8]]


def _get_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]
    for from_v, to_v in edges:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list


def shortest_distance(n, edges, source):
    adj_list = _get_adj_list(n, edges)
    distance = [float('inf')] * n
    distance[source] = 0
    _dfs(adj_list, distance, source)
    return distance


def _dfs(adj_list, distance, source):
    for adj_vertex in adj_list[source]:
        if distance[source] + 1 < distance[adj_vertex]:
            distance[adj_vertex] = distance[source] + 1
            _dfs(adj_list, distance, adj_vertex)


print(shortest_distance(n, edges, 0))


def shortest_path_bfs(n, edges, source):
    adj_list = _get_adj_list(n, edges)
    distance = [float('inf')] * n
    distance[source] = 0
    return _bfs(adj_list, distance, source)


def _bfs(adj_list, distance, source):
    queue = deque()
    queue.append(source)

    while queue:
        current = queue.popleft()
        for adj_vertex in adj_list[current]:
            if distance[adj_vertex] > distance[current] + 1:
                distance[adj_vertex] = distance[current] + 1
                queue.append(adj_vertex)
    return distance


print(shortest_path_bfs(n, edges, 0))
