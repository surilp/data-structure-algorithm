def divide_chocolate(sweetness, k):
    left = min(sweetness)
    right = sum(sweetness)
    result = None
    while left <= right:
        mid = (left + right) // 2
        if num_of_subarrays(sweetness, mid) >= k + 1:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


def num_of_subarrays(nums, target):
    cnt = 0
    total = 0
    for i, num in enumerate(nums):
        total += num
        if total > target:
            cnt += 1
            total = 0
    if total > 0:
        cnt += 1
    return cnt


sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 5

print(divide_chocolate(sweetness, k))

print(num_of_subarrays(sweetness, 6))
