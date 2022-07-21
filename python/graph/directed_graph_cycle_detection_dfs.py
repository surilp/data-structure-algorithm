n = 9
m = [(1, 2), (2, 3), (3, 6), (6, 5), (4, 5), (3, 4), (7, 2), (7, 8), (8, 9), (9, 7)]


def _get_adj_list(n, m):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in m:
        adj_list[from_v].append(to_v)
    return adj_list


def detect_cycle_directed_dfs(n, m):
    adj_list = _get_adj_list(n, m)
    visited = set()
    dfs_visited = set()
    for vertex in range(1, n + 1):
        if vertex not in visited:
            if _detect_cycle_directed_dfs(adj_list, visited, dfs_visited, vertex):
                return True
    return False


def _detect_cycle_directed_dfs(adj_list, visited, dfs_visited, vertex):
    if vertex not in visited:
        visited.add(vertex)
        dfs_visited.add(vertex)
        for adj_vertex in adj_list[vertex]:
            if _detect_cycle_directed_dfs(adj_list, visited, dfs_visited, adj_vertex):
                return True
        dfs_visited.remove(vertex)
        return False
    else:
        if vertex in dfs_visited:
            return True
        return False


print(detect_cycle_directed_dfs(n, m))
