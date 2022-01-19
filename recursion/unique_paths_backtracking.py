grid = [[1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]]


def num_of_ways(grid):
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    current = _get_starting_loc(grid)
    return _num_of_ways(grid, visited, current)


def _get_starting_loc(grid):
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if grid[row_idx][col_idx] == 1:
                return (row_idx, col_idx)


def _num_of_ways(grid, visited, current):
    row_idx, col_idx = current
    visited[row_idx][col_idx] = True

    if grid[row_idx][col_idx] == 2:
        if all_visited(visited):
            return 1
        else:
            return 0

    result = 0
    for row_inc, col_inc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        new_row = row_inc + row_idx
        new_col = col_inc + col_idx

        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and not visited[new_row][new_col]:
            if grid[new_row][new_col] == -1:
                visited[new_row][new_col] = True
            else:
                result += _num_of_ways(grid, visited, (new_row, new_col))
                visited[new_row][new_col] = False
    return result


def all_visited(visited):
    for row in visited:
        if not all(row):
            return False
    return True


print(num_of_ways(grid))
print(num_of_ways([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))
print(num_of_ways([[0, 1], [2, 0]]))
