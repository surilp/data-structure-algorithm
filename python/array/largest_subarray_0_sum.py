def func(array):
    n = len(array)
    if n == 0:
        return n
    hash_map = {array[0]: 0}
    result = 0
    total = array[0]
    for idx in range(1, n):
        num = array[idx]
        total += num
        if total in hash_map:
            result = max(result, idx - hash_map[total])
        else:
            hash_map[total] = idx
    return result


array = [15, -2, 2, -8, 1, 7, 10, 23]

print(func(array))
