from pprint import pprint

# adjacency matrix

'''
1st based index
create N+1 X N+1 matrix
'''


def create_adjacency_matrix(n, m):
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    pprint(matrix)

    for row,col in m:
        matrix[row][col] = 1
        matrix[col][row] = 1

    pprint(matrix)


def create_adjacency_list(n, m):
    array = [[] for _ in range(n + 1)]
    pprint(array)
    for row, col in m:
        array[row].append(col)
        array[col].append(row)
    pprint(array)


n = 5
m = [(1, 2), (2, 3), (2, 4), (3, 4), (5, 3), (1, 3), (1, 5)]

create_adjacency_matrix(n, m)
create_adjacency_list(n, m)
