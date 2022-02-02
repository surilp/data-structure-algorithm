def partition_equal_subset_sum(arr):
    total = sum(arr)
    if total % 2 == 0:
        target = total // 2
        arr_len = len(arr)
        return does_subset_exists_with_sum(arr, arr_len - 1, target)
    else:
        return False


def does_subset_exists_with_sum(arr, n, target):
    if target == 0:
        return True
    if n == 0:
        return arr[n] == target
    pick = False
    if arr[n] <= target:
        pick = does_subset_exists_with_sum(arr, n - 1, target - arr[n])
    not_pick = does_subset_exists_with_sum(arr, n - 1, target)
    return pick or not_pick


arr = [2, 3, 3, 3, 4, 5]
print(partition_equal_subset_sum(arr))

arr = [5, 6, 5, 11, 6]
print(partition_equal_subset_sum(arr))


def canPartition(arr, n):
    total = sum(arr)
    if total % 2 == 0:
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(n)]
        return _canPartition(arr, dp)
    else:
        return False


def _canPartition(arr, dp):
    for n in range(len(dp)):
        dp[n][0] = True
    dp[0][arr[0]] = True
    for n in range(1, len(dp)):
        for target in range(1, len(dp[0])):
            not_pick = dp[n - 1][target]
            pick = False
            if arr[n] <= target:
                pick = dp[n - 1][target - arr[n]]
            dp[n][target] = not_pick or pick
    return dp[len(dp) - 1][len(dp[0]) - 1]


arr = [2, 3, 3, 3, 4, 5]
print(canPartition(arr, 6))
