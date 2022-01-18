n = 5
edges = [
    [1, 2, 9],
    [1, 4, 2],
    [2, 5, 1],
    [4, 2, 4],
    [4, 5, 6],
    [3, 2, 3],
    [5, 3, 7],
    [3, 1, 5]
]

def _get_adj_list(n, edges):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v, weight in edges:
        adj_list[from_v].append([to_v, weight])
    return adj_list

def network_time_delay(n, edges, k):
    adj_list = _get_adj_list(n, edges)
    distance = [float('inf')] * (n + 1)
    distance[k] = 0
    _network_time_delay(adj_list, distance, k)
    return max(distance[1:])

def _network_time_delay(adj_list, distance, k):
    # print(k, distance)
    for adj_vertex, weight in adj_list[k]:
        if distance[adj_vertex] > distance[k] + weight:
            distance[adj_vertex] = distance[k] + weight
            _network_time_delay(adj_list, distance, adj_vertex)


print(network_time_delay(n, edges, 1))