array = [8, 5, 2, 9, 7, 6, 3]
k = 3


def quickselect(array, k):
    return _quickselect(array, 0, len(array) - 1, k - 1)


def _quickselect(array, start, end, k):
    if start > end:
        return -1
    pivot_idx = end
    i = start
    j = start
    pivot_value = array[pivot_idx]
    while j < end:
        if array[j] > pivot_value:
            j += 1
        else:
            array[i], array[j] = array[j], array[i]
            i += 1
            j += 1
    array[i], array[pivot_idx] = array[pivot_idx], array[i]
    pivot_idx = i
    if pivot_idx == k:
        return array[pivot_idx]
    elif k > pivot_idx:
        return _quickselect(array, pivot_idx + 1, end, k)
    else:
        return _quickselect(array, start, pivot_idx - 1, k)


array = [8, 5, 2, 9, 7, 6, 3]
k = 3

print(quickselect(array, k))
