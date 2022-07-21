'''
in degree array
Kahn's Algorithm
'''

from collections import deque


def _get_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]
    in_degree = [0] * n
    for from_v, to_v in edges:
        adj_list[from_v].append(to_v)
        in_degree[to_v] += 1
    return adj_list, in_degree


def topo_sort_bfs(n, edges):
    adj_list, in_degree = _get_adj_list(n, edges)
    result = []
    queue = deque()
    _fill_queue(queue, in_degree)
    while queue:
        current = queue.popleft()
        result.append(current)
        _update_indegree(current, adj_list, in_degree)
        _fill_queue(queue, in_degree)
    if _is_cycle_present(in_degree):
        return []
    else:
        return result


def _is_cycle_present(in_degree):
    for num in in_degree:
        if num >= 0:
            return True
    return False


def _update_indegree(vertex, adj_list, in_degree):
    for adj_vertex in adj_list[vertex]:
        in_degree[adj_vertex] -= 1


def _fill_queue(queue, in_degree):
    for idx in range(len(in_degree)):
        if in_degree[idx] == 0:
            queue.append(idx)
            in_degree[idx] -= 1


n = 6
edges = [[5, 0], [4, 0], [5, 2], [4, 1], [2, 3], [3, 1]]
print(topo_sort_bfs(n, edges))

# cycle
n = 4
edges = [[0, 1], [1, 2], [2, 3], [3, 1]]
print(topo_sort_bfs(n, edges))
