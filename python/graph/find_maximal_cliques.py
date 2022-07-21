'''
Bron-Kerbosch Algorithm
BK(R,P,X)
R = current clique
P = candidate set
X = exclusion set
    if P and X are empty:
        output R
    for each v in p:
        BK(R union {v}, P remove N(v), X remove N(v))

'''

n = 5
edges = [
    [1, 3],
    [1, 2],
    [2, 3],
    [3, 4],
]


def _get_adj_list(n, edges):
    adj_list = [set() for _ in range(n + 1)]
    for from_v, to_v in edges:
        adj_list[from_v].add(to_v)
        adj_list[to_v].add(from_v)
    return adj_list


def find_maximal_cliques(n, edges):
    adj_list = _get_adj_list(n, edges)
    vertices = {v for v in range(1, n + 1)}
    result = []
    bron_kerbosch_algo(adj_list, set(), vertices, set(), result)
    return result


def bron_kerbosch_algo(adj_list, current, candidate, exclusion, result):
    if not candidate and not exclusion:
        result.append(current)
        return
    while candidate:
        vertex = candidate.pop()
        bron_kerbosch_algo(adj_list, current.union({vertex}), candidate.intersection(adj_list[vertex]),
                           exclusion.intersection(adj_list[vertex]), result)
        exclusion.update({vertex})


print(find_maximal_cliques(n, edges))
