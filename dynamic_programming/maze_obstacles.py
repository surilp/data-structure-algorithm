grid = [[0, 0, 0],
        [0, -1, 0],
        [0, 0, 0]]


def maze_obstacle(grid):
    row_idx = len(grid) - 1
    col_dix = len(grid[0]) - 1
    cache = [[None] * len(grid[0]) for _ in range(len(grid))]
    return _maze_obstacle(grid, row_idx, col_dix, cache)


def _maze_obstacle(grid, row, col, cache):
    if row < 0 or col < 0:
        return 0
    if row == col == 0:
        if grid[row][col] == -1:
            return 0
        else:
            return 1
    if grid[row][col] == -1:
        return 0
    if not cache[row][col]:
        cache[row][col] = _maze_obstacle(grid, row - 1, col, cache) + _maze_obstacle(grid, row, col - 1, cache)
    return cache[row][col]


print(maze_obstacle(grid))


def maze_obstacle_v2(grid):
    cache = [[0] * len(grid[0]) for _ in range(len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == col == 0:
                if grid[row][col] == -1:
                    cache[row][col] = 0
                else:
                    cache[row][col] = 1
            elif grid[row][col] == -1:
                cache[row][col] = 0
            else:
                left = _get_value(cache, row, col - 1)
                up = _get_value(cache, row - 1, col)
                cache[row][col] = left + up
    return cache[-1][-1]


def _get_value(cache, row, col):
    if row < 0 or col < 0:
        return 0
    return cache[row][col]


print(maze_obstacle_v2(grid))
