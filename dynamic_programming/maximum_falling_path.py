grid = [
    [1, 2, 10, 4],
    [100, 3, 2, 1],
    [1, 1, 20, 2],
    [1, 2, 2, 1]
]
def maximum(grid):
    if len(grid) == 1:
        return max(grid[0])
    result = -float('inf')
    cache = [[None] * len(grid[0]) for _ in range(len(grid))]
    for col in range(len(grid[0])):
        result = max(result, _maximum(grid, len(grid) - 1, col, cache))

    return result

def _maximum(grid, row, col, cache):
    if col < 0 or col >= len(grid[0]):
        return -float('inf')
    if row == 0:
        return grid[row][col]
    if cache[row][col]:
        return cache[row][col]
    up = _maximum(grid, row - 1, col, cache)
    up_left = _maximum(grid, row - 1, col - 1, cache)
    up_right = _maximum(grid, row - 1, col + 1, cache)
    cache[row][col] = max(up, up_left, up_right) + grid[row][col]
    return cache[row][col]

print(maximum(grid))

def maximum_v2(grid):
    prev = [i for i in grid[0]]

    for row in range(1, len(grid)):
        cur = [None] * len(grid[0])
        for col in range(len(grid)):
            up = prev[col] + grid[row][col]
            up_left = prev[col-1] + grid[row][col] if col - 1 >=0 else -float('inf')
            up_right = prev[col + 1] + grid[row][col] if col + 1 < len(grid[0]) else -float('inf')
            cur[col] = max(up, up_left, up_right)
        prev = cur

    return max(prev)

print(maximum_v2(grid))