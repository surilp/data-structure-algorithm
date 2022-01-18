import heapq

n = 5
edges = [
    [1, [2, 2]],
    [1, [4, 1]],
    [2, [5, 5]],
    [2, [3, 4]],
    [4, [3, 3]],
    [3, [5, 1]]
]


def _get_adj_list(n, edges):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in edges:
        adj_list[from_v].append(to_v)
        adj_list[to_v[0]].append([from_v, to_v[1]])
    return adj_list


def shortest_path_dfs(n, edges, source):
    adj_list = _get_adj_list(n, edges)
    distance = [float('inf')] * (n + 1)
    distance[source] = 0
    _shortest_path_dfs(adj_list, distance, source)
    return distance


def _shortest_path_dfs(adj_list, distance, source):
    for adj_vertex, weight in adj_list[source]:
        if distance[adj_vertex] > distance[source] + weight:
            distance[adj_vertex] = distance[source] + weight
            _shortest_path_dfs(adj_list, distance, adj_vertex)


print(shortest_path_dfs(n, edges, 1))


def dijkstra(n, edges, source):
    adj_list = _get_adj_list(n, edges)
    distance = [float('inf')] * (n + 1)
    visited = set()
    distance[source] = 0
    heap_queue = [(0, source)]
    heapq.heapify(heap_queue)

    while heap_queue:
        current_weight, current_vertex = heapq.heappop(heap_queue)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for adj_vertex, weight in adj_list[current_vertex]:
            if current_weight + weight < distance[adj_vertex]:
                distance[adj_vertex] = current_weight + weight
                heapq.heappush(heap_queue, (distance[adj_vertex], adj_vertex))
    return distance


print(dijkstra(n, edges, 1))
