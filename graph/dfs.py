from Graph import Graph

n = 7
m = [(1, 2), (2, 4), (2, 7), (4, 6), (7, 6), (3, 5)]


def dfs(n, m):
    adj_list = Graph.get_adj_list(n, m)
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
