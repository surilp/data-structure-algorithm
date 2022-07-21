'''

on node removal graph is broken into two or more components

low adj >= time in current and parent is not None

'''


class Timer:
    CURRENT = 0

    def get_time(self):
        Timer.CURRENT += 1
        return Timer.CURRENT


def create_adj_list(n, edges):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in edges:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list


def find_articulation_points(n, edges):
    adj_list = create_adj_list(n, edges)
    visited = [False] * (n + 1)
    time_in = [None] * (n + 1)
    lowest_time = [None] * (n + 1)
    result = set()
    timer = Timer()
    for vertex in range(1, n + 1):
        if not visited[vertex]:
            _dfs(adj_list, visited, time_in, lowest_time, result, vertex, None, timer)
    return result


def _dfs(adj_list, visited, time_in, lowest_time, result, vertex, parent, timer):
    visited[vertex] = True
    time_in[vertex] = timer.get_time()
    lowest_time[vertex] = time_in[vertex]
    individual_children = 0
    for adj_ver in adj_list[vertex]:
        if not visited[adj_ver]:
            individual_children += 1
            _dfs(adj_list, visited, time_in, lowest_time, result, adj_ver, vertex, timer)
            if parent != adj_ver:
                lowest_time[vertex] = min(lowest_time[vertex], lowest_time[adj_ver])
                if lowest_time[adj_ver] >= time_in[vertex] and parent is not None:
                    result.add(vertex)
                if parent is None and individual_children > 1:
                    result.add(vertex)

        else:
            if parent != adj_ver:
                lowest_time[vertex] = time_in[adj_ver]


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
print(find_articulation_points(n, edges))

n = 10
edges = [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6],
    [5, 6],
    [3, 7],
    [3, 8],
    [7, 8],
    [4, 9],
    [4, 10],
    [9, 10]
]
print(find_articulation_points(n, edges))
