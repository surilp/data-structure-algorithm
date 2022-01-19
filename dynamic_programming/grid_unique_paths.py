'''
count paths
count paths with obstacles
minimum path sum
max path sum
triangle
2 start points
'''


# memoization
def count_paths(n):
    cache = [[None] * n for _ in range(n)]
    return _count_paths(n - 1, n - 1, cache)


def _count_paths(row, col, cache):
    if cache[row][col]:
        return cache[row][col]

    if row == 0 and col == 0:
        return 1
    if row < 0 or col < 0:
        return 0

    cache[row][col] = _count_paths(row, col - 1, cache) + _count_paths(row - 1, col, cache)
    return cache[row][col]


print(count_paths(3))


# tabulation

def count_paths_v2(n):
    cache = [[None] * n for _ in range(n)]
    for row_idx in range(len(cache)):
        for col_idx in range(len(cache[0])):
            if row_idx == 0 and col_idx == 0:
                cache[row_idx][col_idx] = 1
            else:
                left = _get_ways(cache, row_idx, col_idx - 1)
                up = _get_ways(cache, row_idx - 1, col_idx)
                cache[row_idx][col_idx] = left + up
    return cache[n - 1][n - 1]


def _get_ways(cache, row, col):
    if row < 0 or col < 0:
        return 0
    else:
        return cache[row][col]


print(count_paths_v2(3))


# space optimization
def count_paths_v3(n):
    current = [None] * n
    prev = [None] * n

    for row_idx in range(n):
        for col_idx in range(n):
            if row_idx == 0 and col_idx == 0:
                current[0] = 1
            else:
                left = _get_ways_v3(current, col_idx - 1)
                up = _get_ways_v3(prev, col_idx)
                current[col_idx] = left + up
        prev = current
        current = [None] * n
    return prev[n - 1]


def _get_ways_v3(arr, idx):
    if idx < 0 or arr[idx] is None:
        return 0
    else:
        return arr[idx]


print(count_paths_v3(3))
