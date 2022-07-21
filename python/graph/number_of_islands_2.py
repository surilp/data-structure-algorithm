from graph.disjoint_set import DSU


def count_number_of_islands(n, m, operations):
    grid = [[0] * m for _ in range(n)]
    row_len = n
    col_len = m
    dsu = DSU(row_len * col_len)
    result = []
    islands = 0
    for row, col in operations:
        grid[row][col] = 1
        count = get_neighbour_island(grid, row, col, dsu, col_len)
        if count == 0:
            islands += 1
        else:
            islands = islands - count + 1
        result.append(islands)
    return result


def get_idx(row, col, col_len):
    return (row * col_len) + col


def get_neighbour_island(grid, row, col, dsu, col_len):
    idx = get_idx(row, col, col_len)
    result = set()
    for row_inc, col_inc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        new_row = row_inc + row
        new_col = col_inc + col
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 1:
            new_idx = get_idx(new_row, new_col, col_len)
            result.add(dsu.find_parent(new_idx))
    for item in result:
        dsu.union(item, idx)
    return len(result)


n = 3
m = 3
operations = [
    (0, 0),
    (0, 1),
    (1, 2),
    (2, 0),
    (1, 1)
]
print(count_number_of_islands(n, m, operations))

n = 3
m = 3
operations = [
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 2),
    (2, 2),
    (1, 1)
]
print(count_number_of_islands(n, m, operations))

n = 4
m = 5
operations = [[1, 1], [0, 1], [3, 3], [3, 4]]
print(count_number_of_islands(n, m, operations))

n = 3
m = 3
operations = [[0, 0], [0, 1], [2, 2], [2, 1]]
print(count_number_of_islands(n, m, operations))
