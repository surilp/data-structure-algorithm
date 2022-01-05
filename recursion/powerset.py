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



print(powerset([1,2,3]))