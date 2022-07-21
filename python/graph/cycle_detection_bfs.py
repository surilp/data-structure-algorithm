from collections import deque


n = 11
m = [(1, 2), (2, 4), (3, 5), (5, 6), (5, 10), (6, 7), (10, 9), (7, 8), (9, 8), (8, 11)]

def _get_adj_list(n, m):
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in m:
        adj_list[from_v].append(to_v)
        adj_list[to_v].append(from_v)
    return adj_list

def detect_cyle_bfs(n, m):
    adj_list = _get_adj_list(n, m)
    visited = [False] * (n + 1)
    for vertex in range(1, n+1):
        if not visited[vertex]:
            queue = deque()
            queue.append((vertex, None))
            visited[vertex] = True
            if _detect_cycle_bfs(adj_list, queue, visited):
                return True
    return False


def _detect_cycle_bfs(adj_list, queue, visited):
    while queue:
        current_vertex, parent = queue.popleft()
        for adj_vertex in adj_list[current_vertex]:
            if not visited[adj_vertex]:
                visited[adj_vertex] = True
                queue.append((adj_vertex, current_vertex))
            elif visited[adj_vertex] and adj_vertex != parent:
                print(adj_vertex, parent)
                return True
    return False

print(detect_cyle_bfs(n, m))
