n = 8
m = [(1, 3), (3, 4), (2, 5), (5, 8), (5, 6), (8, 7), (7, 6)]


def _get_adj_list(n, m):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in m:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list


def detect_cycle_dfs(n, m):
    adj_list = _get_adj_list(n, m)
    visited = [False] * (n + 1)
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            if _detect_cycle_dfs(adj_list, visited, vertex, None):
                return True
    return False


def _detect_cycle_dfs(adj_list, visited, vertex, parent):
    if not visited[vertex]:
        visited[vertex] = True
        for adj_vertex in adj_list[vertex]:
            if not visited[adj_vertex]:
                return _detect_cycle_dfs(adj_list, visited, adj_vertex, vertex)
            elif visited[adj_vertex] and adj_vertex != parent:
                print(adj_vertex, parent)
                return True
    return False


print(detect_cycle_dfs(n, m))
