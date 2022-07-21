from collections import defaultdict


def alien_dictionary(words):
    adj_list = build_adj_list(words)
    visited = set()
    dfs_visited = set()
    stack = []
    def dfs(node):
        visited.add(node)
        dfs_visited.add(node)
        for adj_node in adj_list[node]:
            if adj_node not in visited:
                dfs(adj_node)
        dfs_visited.remove(node)
        stack.append(node)
    for let in list(adj_list.keys()):
        if let not in visited:
            dfs(let)
    stack.reverse()
    return stack



def build_adj_list(words):
    adj_list = defaultdict(list)
    for idx in range(1, len(words)):
        cur = words[idx]
        cur_len = len(cur)
        prev = words[idx - 1]
        prev_len = len(prev)
        i = 0
        j = 0
        while i < cur_len and j < prev_len and cur[i] == prev[j]:
            i += 1
            j += 1
        if i == j and i < cur_len and j < prev_len:
            adj_list[prev[j]].append(cur[i])
    return adj_list







words = ["wrt", "wrf", "er", "ett", "rftt"]
print(alien_dictionary(words))

