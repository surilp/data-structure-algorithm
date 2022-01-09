n = 7
m = [(1, 2), (2, 4), (2, 7), (4, 6), (7, 6), (3, 5)]


def _create_adj_list(n, m):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in m:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list


def dfs(n, m):
    adj_list = _create_adj_list(n, m)
    visited = [False] * (n + 1)
    result = []
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            _dfs(vertex, adj_list, visited, result)
    return result


def _dfs(current_vertex, adj_list, visited, result):
    result.append(current_vertex)
    visited[current_vertex] = True
    for adj_vertex in adj_list[current_vertex]:
        if not visited[adj_vertex]:
            _dfs(adj_vertex, adj_list, visited, result)


print(dfs(n, m))
