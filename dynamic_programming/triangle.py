triangle = [
    [1],
    [2, 3],
    [3, 6, 7],
    [8, 9, 6, 10]
]


def triangle_memoization(data):
    row = len(data) - 1
    cache = [[None] * len(row) for row in data]
    result = _triangle_memoization(data, row, None, cache)
    return result


def _triangle_memoization(data, row, col, cache):
    if row == 0:
        return data[0][0]
    if col and (col < 0 or col >= len(data[row])):
        return float('inf')
    if col and cache[row][col]:
        return cache[row][col]
    result = float('inf')
    for col in range(len(data[row])):
        temp = min(_triangle_memoization(data, row - 1, col - 1, cache),
                   _triangle_memoization(data, row - 1, col, cache)) + data[row][col]
        cache[row][col] = temp
        result = min(temp, result)
    return result


print(triangle_memoization(triangle))


def triangle_tabulation(triangle):
    row_len = len(triangle) -1
    cache = [[None] * len(row) for row in triangle]
    for col in range(len(triangle[row_len])):
        cache[row_len][col] = triangle[row_len][col]
    for row in range(row_len - 1, -1, -1):
        for col in range(len(triangle[row])):
            down = cache[row+1][col]
            dia = cache[row+1][col+1]
            cache[row][col] = min(down, dia) + triangle[row][col]
    return cache[0][0]


print(triangle_tabulation(triangle))