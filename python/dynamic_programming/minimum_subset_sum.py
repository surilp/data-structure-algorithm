def minimum_subset_sum(arr, n):
    total = sum(arr)
    dp = [[False] * (total + 1) for _ in range(n)]
    for row in range(n):
        dp[row][0] = True
    if arr[0] < total:
        dp[0][arr[0]] = True
    for row in range(1, n):
        for target in range(1, total + 1):
            not_pick = dp[row - 1][target]
            pick = False
            if arr[row] <= target:
                pick = dp[row - 1][target - arr[row]]
            dp[row][target] = pick or not_pick
    result = float('inf')
    for target in range(total + 1):
        value = dp[n - 1][target]
        if value:
            result = min(result, abs((total - target) - target))
    return result


arr = [1, 2, 3, 4]
print(minimum_subset_sum(arr, len(arr)))


arr = [8,6,5]
print(minimum_subset_sum(arr, len(arr)))