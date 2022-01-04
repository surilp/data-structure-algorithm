'''
a contiguous sequence which follows order
a non contiguous sequence which follows order
'''


def subsequence(arr, result=[[]]):
    if not arr:
        return result

    temp_result = subsequence(arr[1:], result)
    for idx in range(len(temp_result)):
        result.append([arr[0]] + temp_result[idx])

    return result


# print(subsequence([3, 2 , 1]))


def subsequence(arr, idx, temp_result, result):
    if idx >= len(arr):
        result.append(temp_result.copy())
        return

    temp_result.append(arr[idx])
    subsequence(arr, idx + 1, temp_result, result)
    temp_result.pop()
    subsequence(arr, idx + 1, temp_result, result)


result = []
subsequence([3, 2, 1], 0, [], result)


# print(result)


def subsequence_k_sum(arr, idx, temp_result, k, s):
    if idx >= len(arr):
        if s == k:
            print(temp_result)
        return

    temp_result.append(arr[idx])
    subsequence_k_sum(arr, idx + 1, temp_result, k, s + arr[idx])
    temp_result.pop()
    subsequence_k_sum(arr, idx + 1, temp_result, k, s)


# subsequence_k_sum([1,2,1,2,4], 0, [], 4, 0)


def subsequence_k_sum_one(arr, idx, temp_result, k, s):
    if idx >= len(arr):
        if s == k:
            print(temp_result)
            return True
        return False

    temp_result.append(arr[idx])
    if subsequence_k_sum_one(arr, idx + 1, temp_result, k, s + arr[idx]):
        return True
    temp_result.pop()
    if subsequence_k_sum_one(arr, idx + 1, temp_result, k, s):
        return True
    return False


# subsequence_k_sum_one([1, 2, 1, 2, 4], 0, [], 4, 0)


def subsequence_count(arr, idx, k, s):
    if idx >= len(arr):
        if s == k:
            return 1
        return 0

    left = subsequence_count(arr, idx + 1, k, s + arr[idx])
    right = subsequence_count(arr, idx + 1, k, s)

    return left + right


print(subsequence_count([1, 2, 1], 0, 2, 0))
