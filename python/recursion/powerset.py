def powerset(array):
    result = []
    _powerset(array, 0, [], result)
    return result


def _powerset(array, idx, ds, result):
    if idx >= len(array):
        result.append(list(ds))
        return
    ds.append(array[idx])
    _powerset(array, idx + 1, ds, result)
    ds.pop()
    _powerset(array, idx + 1, ds, result)


def powerset_bit(array):
    array_len = len(array)
    result = []
    temp = [''] * array_len
    for num in range(2 ** array_len):
        for idx in range(array_len - 1, -1, -1):
            if is_bit_set(num, idx):
                temp[idx] = array[idx]
            else:
                temp[idx] = ''
        result.append(''.join(map(str, temp)))
    return result


def is_bit_set(num, pos):
    return num & (1 << pos) != 0


print(powerset([1, 2, 3]))
print(powerset_bit([1, 2, 3]))
