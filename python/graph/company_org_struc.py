from collections import defaultdict
from collections import deque


def find_all_sub(org, emp):
    org = org.split(';')
    org = list(map(lambda x: list(map(int, x.split(','))), org))
    adj_list = create_adj_list(org)
    result = []
    _bfs(adj_list, result, emp)
    return result if result else 'NO'


def _dfs(adj_list, result, idx):
    for adj_idx in adj_list[idx]:
        result.append(adj_idx)
        _dfs(adj_list, result, adj_idx)


def _bfs(adj_list, result, emp):
    queue = deque()
    for subor in adj_list[emp]:
        queue.append(subor)
    while queue:
        current = queue.popleft()
        result.append(current)
        for subor in adj_list[current]:
            queue.append(subor)
    return result


def create_adj_list(org):
    adj_map = defaultdict(list)
    for report, supervisor in org:
        adj_map[supervisor].append(report)
    return adj_map


org = '2,1;3,1;4,1;5,3;6,3;7,3;8,5;9,5;10,5'
emp = 3
print(find_all_sub(org, emp))

org = '2,1;3,1;4,1;5,3;6,3;7,3;8,5;9,5;10,5'
emp = 8
print(find_all_sub(org, emp))
