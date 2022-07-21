from collections import deque


def _get_adj_list(n, m):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in m:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list


def bipartite_graph_bfs(n, m):
    adj_list = _get_adj_list(n, m)
    visited = [False] * (n + 1)
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            if not _bipartite_graph_bfs(adj_list, vertex, visited):
                return False
    return True


def _bipartite_graph_bfs(adj_list, vertex, visited):
    queue = deque()
    queue.append(vertex)
    visited[vertex] = 1

    while queue:
        current_vertex = queue.popleft()
        for adj_vertex in adj_list[current_vertex]:
            if not visited[adj_vertex]:
                adj_color = 1 if visited[current_vertex] == 2 else 2
                visited[adj_vertex] = adj_color
                queue.append(adj_vertex)
            else:
                if visited[current_vertex] == visited[adj_vertex]:
                    return False
    return True


n = 8
m = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (2, 8), (8, 5)]
print(bipartite_graph_bfs(n, m))

n = 8
m = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 8), (2, 7), (7, 6), (6, 5)]
print(bipartite_graph_bfs(n, m))