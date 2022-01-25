'''
time of insertion - dfs - array
lowest time of insertion - array

low adjacent > time of insertion of vertex
'''

n = 12
edges = [
    [1, 2],
    [1, 4],
    [4, 3],
    [2, 3],
    [4, 5],
    [5, 6],
    [6, 7],
    [6, 9],
    [7, 8],
    [9, 8],
    [8, 10],
    [10, 11],
    [10, 12],
    [11, 12]
]


class Counter:
    count = 0

    def get_counter(self):
        Counter.count += 1
        return Counter.count


def _get_adj_list(n, edges):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in edges:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list


def find_bridges(n, edges):
    adj_list = _get_adj_list(n, edges)
    time_in = [None] * (n + 1)
    lowest_time = [None] * (n + 1)
    bridges = []
    counter = Counter()
    parent = None
    for vertex in range(1, n + 1):
        if time_in[vertex] is None:
            _find_bridges(adj_list, time_in, lowest_time, vertex, bridges, counter, parent)
    return bridges


def _find_bridges(adj_list, time_in, lowest_time, vertex, bridges, counter, parent):
    time_in[vertex] = counter.get_counter()
    lowest_time[vertex] = time_in[vertex]
    for adj_vertex in adj_list[vertex]:
        if adj_vertex == parent:
            continue
        if time_in[adj_vertex] is None:
            _find_bridges(adj_list, time_in, lowest_time, adj_vertex, bridges, counter, vertex)
            lowest_time[vertex] = min(lowest_time[vertex], lowest_time[adj_vertex])
            if lowest_time[adj_vertex] > time_in[vertex]:
                bridges.append((vertex, adj_vertex))
        else:
            lowest_time[vertex] = min(lowest_time[adj_vertex], lowest_time[vertex])


print(find_bridges(n, edges))
