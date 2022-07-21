'''
MST
graph has to be weighted graph
convert graph to tree such that n nodes and n-1 edges

start with first node
check min edge attached to this node
now adjacent edges of both the node fidn minimal


three arrays
1) key = all to infinity
2) MST = all to False
3) parent = all to -1

- minimum index with value and not visisted - min(key) and MST[key] = F
mark MST key to True
iterate through adjacent node
update key value
update parent

scroll through key array
'''
from heapq import heappop, heappush, heapify

n = 5
edges = [
    [0, [1, 2]],
    [0, [3, 6]],
    [3, [1, 8]],
    [1, [2, 3]],
    [1, [4, 5]],
    [4, [2, 7]],
]


def _get_adj_list(n, edges):
    adj_list = [[] for _ in range(n)]
    for from_v, to_v in edges:
        adj_list[from_v].append(to_v)
        adj_list[to_v[0]].append([from_v, to_v[1]])
    return adj_list


def prims(n, edges):
    adj_list = _get_adj_list(n, edges)
    key = [float('inf')] * n
    key[0] = 0
    mst = [False] * n
    parent = [-1] * n
    priority_queue = [(0, 0)]
    heapify(priority_queue)
    _prim(adj_list, key, mst, parent, priority_queue)
    return get_graph(parent)


def _prim(adj_list, key, mst, parent, priority_queue):
    while priority_queue:
        current_weight, current_vertex = heappop(priority_queue)
        mst[current_vertex] = True
        for adj_vertex, weight in adj_list[current_vertex]:
            if not mst[adj_vertex] and key[adj_vertex] > weight:
                key[adj_vertex] = weight
                parent[adj_vertex] = current_vertex
                heappush(priority_queue, (key[adj_vertex], adj_vertex))


def get_lowest_key_vertex(key, mst):
    min_val = float('inf')
    result = None
    for idx in range(len(key)):
        if not mst[idx] and key[idx] < min_val:
            min_val = key[idx]
            result = idx
    return result


def get_graph(parent):
    result = []
    for idx, val in enumerate(parent):
        if val != -1:
            result.append([val, idx])
    return result

print(prims(n ,edges))