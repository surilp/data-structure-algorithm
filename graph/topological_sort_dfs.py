



def _get_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]
    for from_v, to_v in edges:
        adj_list[from_v].append(to_v)
    return adj_list

def topo_sort_dfs(n, edges):
    adj_list = _get_adj_list(n, edges)
    visited = [False] * n
    dfs_visited = [False] * n
    result = []
    for vertex in range(n):
        if not visited[vertex]:
            if not _topo_sort_dfs(adj_list, visited, result, vertex, dfs_visited):
                return []
    return result[::-1]



def _topo_sort_dfs(adj_list, visited, result, vertex, dfs_visited):
    visited[vertex] = True
    dfs_visited[vertex] = True
    for adj_vertex in adj_list[vertex]:
        if not visited[adj_vertex]:
            if not _topo_sort_dfs(adj_list, visited, result, adj_vertex, dfs_visited):
                return False
            dfs_visited[adj_vertex] = False
        else:
            if dfs_visited[adj_vertex]:
                return False
    dfs_visited[vertex] = False
    result.append(vertex)
    return True



n = 6
edges = [[5, 0], [4, 0], [5, 2], [4, 1], [2, 3], [3, 1]]
print(topo_sort_dfs(n, edges))


# cycle
n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 1]]
print(topo_sort_dfs(n, edges))