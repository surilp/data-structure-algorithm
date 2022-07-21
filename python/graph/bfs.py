from collections import deque


def _get_adj_list(n, m):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in m:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list


n = 7
m = [(1, 2), (2, 3), (2, 7), (3, 5), (7, 5), (4, 6)]


def bfs(n, m):
    adj_list = _get_adj_list(n, m)
    visited = [False] * (n + 1)
    result = []

    for idx in range(1, n + 1):
        if not visited[idx]:
            queue = deque()
            queue.append(idx)
            visited[idx] = True
            _bfs(adj_list, queue, visited, result)

    return result

def _bfs(adj_list, queue, visited, result):
    while queue:
        current = queue.popleft()
        result.append(current)
        for adj in adj_list[current]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)

print(bfs(n, m))
