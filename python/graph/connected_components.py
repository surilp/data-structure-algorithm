'''
disconnected graph with multiple components

take visited array of size n
all will be marked false
traverse all nodes in this array

traverse 1 to 10
if not visited
do dfs/bfs

'''

n = 10
m = [(1, 3), (3, 4), (4, 6), (6, 8), (2, 9), (5, 7), (7, 10)]


def find_number_of_components(n, m):
    visited = [False for _ in range(n + 1)]
    adj_list = [[] for _ in range(n + 1)]
    for from_v, to_v in m:
        adj_list[from_v].append(to_v)
    result = 0
    for idx in range(1, len(visited)):
        if _dfs(visited, adj_list, idx):
            result += 1
    return result

def _dfs(visited, adj_list, idx):
    flag = False
    if not visited[idx]:
        visited[idx] = True
        for neighbour in adj_list[idx]:
            flag = True
            _dfs(visited, adj_list, neighbour)
    return flag

print(find_number_of_components(n,m))