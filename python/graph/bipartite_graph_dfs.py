def _get_adj_list(n, m):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in m:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list


def bipartite_graph_dfs(n, m):
    adj_list = _get_adj_list(n, m)
    color = [None] * (n + 1)
    for vertex in range(1, n + 1):
        if not color[vertex]:
            color[vertex] = 0
            if not _bipartite_graph_dfs(adj_list, color, vertex):
                return False
    return True


def _bipartite_graph_dfs(adj_list, color, vertex):
    for adj_vertex in adj_list[vertex]:
        if color[adj_vertex] is None:
            color[adj_vertex] = 1 - color[vertex]
            if not _bipartite_graph_dfs(adj_list, color, adj_vertex):
                return False
        elif color[adj_vertex] == color[vertex]:
            print(f'adj vertex {adj_vertex} and vertex {vertex}')
            return False
    return True


n = 8
m = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (2, 8), (8, 5)]
print(bipartite_graph_dfs(n, m))

n = 8
m = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 8), (2, 7), (7, 6), (6, 5)]
print(bipartite_graph_dfs(n, m))
