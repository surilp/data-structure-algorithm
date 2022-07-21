def permutation(arr):
    result = []
    map = {item: True for item in arr}
    _permutation(arr, map, [], result)
    return result


def _permutation(arr, map, ds, result):
    if len(ds) == len(arr):
        result.append(list(ds))
        return

    for num, eligible in map.items():
        if eligible:
            ds.append(num)
            map[num] = False
            _permutation(arr, map, ds, result)
            ds.pop()
            map[num] = True


# print(permutation([1, 2, 3]))


def permutation_v2(arr):
    result = []
    _permutation_v2(arr, 0, result)
    return result


def _permutation_v2(arr, idx, result):
    if idx >= len(arr):
        result.append(list(arr))
        return

    for i in range(idx, len(arr)):
        arr[i], arr[idx] = arr[idx], arr[i]
        _permutation_v2(arr, idx + 1, result)
        arr[i], arr[idx] = arr[idx], arr[i]


print(permutation_v2([1, 2, 3]))
