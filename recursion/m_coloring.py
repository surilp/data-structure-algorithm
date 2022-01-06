from collections import defaultdict

def m_coloring(edges, m, n):
    adj_list = get_adj_list(edges)
    vertex_color = {num + 1: None for num in range(n)}
    res = _m_coloring(1,adj_list, vertex_color, m, n)
    return 1 if res else 0


def _m_coloring(current, adj_list, vertex_color, m, n):
    print(vertex_color)
    if all(vertex_color.values()):
        return True

    if vertex_color[current] is None:
        for color in range(1, m + 1):
            vertex_color[current] = color
            if is_valid(adj_list, current, vertex_color, color):
                for dest in adj_list[current]:
                    if _m_coloring(dest, adj_list, vertex_color, m, n):
                        return True
            vertex_color[current] = None
    return False


def is_valid(adj_list, current, vertex_color, color):
    for vertex in adj_list[current]:
        if vertex_color[vertex] == color:
            return False
    return True

def get_adj_list(edges):
    result = defaultdict(list)
    for source, dest in edges:
        result[source].append(dest)
        result[dest].append(source)
    return result



def m_coloring_v2(edges, m, n):
    adj_list = get_adj_list(edges)
    vertex_color = {num:None for num in range(1, n+1)}
    return _m_coloring_v2(1, adj_list, vertex_color, m, n)

def _m_coloring_v2(current_vertex, adj_list, vertex_color, m, n):
    print(vertex_color)
    if current_vertex > n:
        return True

    for color in range(1, m +1):
        vertex_color[current_vertex] = color
        if is_valid(adj_list, current_vertex, vertex_color, color):
            if _m_coloring_v2(current_vertex + 1, adj_list,vertex_color, m, n):
                return True
        vertex_color[current_vertex] = None
    return False



edges = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 1),
    (1, 3)
]


print(m_coloring_v2(edges, m = 2, n =4))