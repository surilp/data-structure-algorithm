points = [
    [2, 1, 3],
    [3, 4, 6],
    [10, 1, 6],
    [8, 3, 7]
]


def ninja_training_v1(points):
    cache = {}
    return _ninja_training_v1(points, len(points) - 1, -1, cache)


def _ninja_training_v1(points, n, picked, cache):
    if (n, picked) in cache:
        return cache[(n, picked)]
    if n == 0:
        result = 0
        for idx in range(3):
            if idx != picked:
                result = max(result, points[n][idx])
        cache[(n, picked)] = result
        return cache[(n, picked)]
    result = 0
    for idx in range(3):
        if idx != picked:
            result = max(_ninja_training_v1(points, n - 1, idx, cache) + points[n][idx], result)
    return result


print(ninja_training_v1(points))



def ninja_training_v2(points):
    if len(points) == 1:
        return max(points[0])
    prev_max = fill_max(points[0])
    current_max = [None] * 3
    for idx in range(1, len(points)):
        for point_idx in range(3):
            current_max[point_idx] = prev_max[point_idx] + points[idx][point_idx]
        prev_max = fill_max(current_max)
    return max(prev_max)

def fill_max(array):
    final = [None] * len(array)
    for idx in range(len(array)):
        result = 0
        for inner_idx in range(len(array)):
            if idx != inner_idx:
                result = max(result, array[inner_idx])
        final[idx] = result
    return final


print(ninja_training_v2(points))