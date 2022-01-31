'''
Strongly connected component

if you start from one node you can reach to all nodes in that component
dfs from back nodes

1) sort all nodes in order of finishing time (topological sort)
2) transpose the graph - all edges will be reversed
3) DFS according to the finish time
'''

n = 5
edges = [
    [1, 2],
    [3, 1],
    [2, 3],
    [2, 4],
    [4, 5]
]


def create_adj_list(n, edges, reverse=False):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in edges:
        if reverse:
            adj_list[to_v].append(from_v)
        else:
            adj_list[from_v].append(to_v)
    return adj_list


def kosaraju_algo(n, edges):
    adj_list = create_adj_list(n, edges, reverse=False)

    # toposort
    visited = [False] * (n + 1)
    topo_sorted = []
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            toposort(adj_list, visited, vertex, topo_sorted)
    print(topo_sorted)

    # transpose
    adj_list_transpose = create_adj_list(n, edges, reverse=True)

    # DFS according to topo sort
    visited = [False] * (n + 1)
    result = []
    while topo_sorted:
        vertex = topo_sorted.pop()
        if not visited[vertex]:
            ds = []
            dfs(adj_list_transpose, visited, vertex, ds, result)
            if ds:
                result.append(ds)
    return result


def toposort(adj_list, visited, vertex, result):
    visited[vertex] = True
    for adj_vertex in adj_list[vertex]:
        if not visited[adj_vertex]:
            toposort(adj_list, visited, adj_vertex, result)
    result.append(vertex)


def dfs(adj_list, visited, vertex, ds, result):
    ds.append(vertex)
    visited[vertex] = True
    for adj_v in adj_list[vertex]:
        if not visited[adj_v]:
            dfs(adj_list, visited, adj_v, ds, result)


print(kosaraju_algo(n, edges))
