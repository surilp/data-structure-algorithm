def find_matching_subarray(pattern, arr):
    pattern_set = set(pattern)
    temp_set = set()
    result = []
    for idx in range(len(arr)):
        temp_set.add(arr[idx])
        if temp_set.issubset(pattern_set):
            if temp_set == pattern_set:
                result.append(idx - len(pattern) + 1)
                temp_set = {arr[idx]}
        else:
            temp_set = set()
    return result


pattern = [1, 0]
arr = [1, 0, 2, 1, 0, 1]
print(find_matching_subarray(pattern, arr))
