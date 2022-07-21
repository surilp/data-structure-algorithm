def reverse_array(arr, idx=0, result=[]):
    if idx >= len(arr):
        return
    reverse_array(arr, idx + 1, result)
    result.append(arr[idx])
    return result


print(reverse_array([1, 2, 3, 4, 2]))


def reverse_array_v1(arr):
    helper(arr, 0, len(arr) - 1)
    return arr


def helper(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        helper(arr, start + 1, end - 1)


print(reverse_array_v1([1, 2, 3, 4, 2]))
