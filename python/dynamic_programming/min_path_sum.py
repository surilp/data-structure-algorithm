def min_sum_path(grid):
    row_idx = len(grid) - 1
    col_idx = len(grid[0]) - 1
    cache = [[None] * len(grid[0]) for _ in range(len(grid))]
    return _min_sum_path(grid, row_idx, col_idx, cache)


def _min_sum_path(grid, row_idx, col_idx, cache):
    if row_idx < 0 or col_idx < 0:
        return float('inf')
    if row_idx == col_idx == 0:
        return grid[row_idx][col_idx]

    if not cache[row_idx][col_idx]:
        cache[row_idx][col_idx] = min(_min_sum_path(grid, row_idx - 1, col_idx, cache),
                                      _min_sum_path(grid, row_idx, col_idx - 1, cache)) + \
                                  grid[row_idx][col_idx]

    return cache[row_idx][col_idx]


def min_sum_path_v2(grid):
    cache = [[None] * len(grid[0]) for _ in range(len(grid))]
    for row_idx in range(len(grid)):
        for col_idx in range(len(grid[0])):
            if row_idx == col_idx == 0:
                cache[row_idx][col_idx] = grid[row_idx][col_idx]
            else:
                left = cache[row_idx][col_idx - 1] if col_idx - 1 >= 0 else float('inf')
                up = cache[row_idx - 1][col_idx] if row_idx - 1 >= 0 else float('inf')
                cache[row_idx][col_idx] = min(left, up) + grid[row_idx][col_idx]
    return cache[-1][-1]


grid = [
    [10, 8, 2],
    [10, 5, 100],
    [1, 1, 2]
]

print(min_sum_path(grid))
print(min_sum_path_v2(grid))
