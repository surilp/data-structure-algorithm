grid = [
    [2, 3, 1, 2],
    [3, 4, 2, 2],
    [5, 6, 3, 5],
]


def cherry_pick(grid):
    cache = create_cache(len(grid), len(grid[0]))
    return _cherry_pick(grid, 0, 0, len(grid[0]) - 1, cache)


def create_cache(n, m):
    result = []
    for row in range(n):
        temp = []
        for col1 in range(m):
            temp2 = [None] * m
            temp.append(temp2)
        result.append(temp)
    return result


def _cherry_pick(grid, row, a_col, b_col, cache):
    if a_col >= len(grid[0]) or a_col < 0 or b_col >= len(grid[0]) or b_col < 0:
        return -float('inf')
    if row == len(grid) - 1:
        if a_col == b_col:
            return grid[row][a_col]
        else:
            return grid[row][a_col] + grid[row][b_col]
    if cache[row][a_col][b_col]:
        return cache[row][a_col][b_col]
    result = -float('inf')
    for inc_a_col in [-1, 0, 1]:
        new_a_col = a_col + inc_a_col
        for inc_b_col in [-1, 0, 1]:
            new_b_col = b_col + inc_b_col
            temp = _cherry_pick(grid, row + 1, new_a_col, new_b_col, cache)
            if a_col == b_col:
                result = max(result, temp + grid[row][a_col])
            else:
                result = max(result, temp + grid[row][a_col] + grid[row][b_col])
    cache[row][a_col][b_col] = result
    return result


print(cherry_pick(grid))


def cherry_pick_tabulation(grid):
    row_len = len(grid)
    col_len = len(grid[0])
    dp = create_cache(row_len, col_len)
    for a_col in range(col_len):
        for b_col in range(col_len):
            if a_col == b_col:
                dp[row_len - 1][a_col][b_col] = grid[row_len - 1][a_col]
            else:
                dp[row_len - 1][a_col][b_col] = grid[row_len - 1][a_col] + grid[row_len - 1][b_col]
    for row in range(row_len - 2, -1, -1):
        for a_col in range(col_len):
            for b_col in range(col_len):
                result = -float('inf')
                for inc_a_col in [-1, 0, 1]:
                    new_a_col = a_col + inc_a_col
                    for inc_b_col in [-1, 0, 1]:
                        new_b_col = b_col + inc_b_col
                        temp = dp[row + 1][new_a_col][
                            new_b_col] if 0 <= new_a_col < col_len and 0 <= new_b_col < col_len else -float('inf')
                        if a_col == b_col:
                            result = max(result, temp + grid[row][a_col])
                        else:
                            result = max(result, temp + grid[row][a_col] + grid[row][b_col])
                dp[row][a_col][b_col] = result
    return dp[0][0][col_len - 1]


print(cherry_pick_tabulation(grid))
