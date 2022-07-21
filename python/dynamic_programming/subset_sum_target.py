'''
subset - contiguous or non contiguous
express in terms of index
explore all possibilities
if any of the return true, return true
'''


def is_subset_with_target(arr, k):
    arr_len = len(arr)
    dp = [[None] * (k + 1) for _ in range(arr_len)]
    return _is_subset_with_target(arr, arr_len - 1, k, dp)


def _is_subset_with_target(arr, n, k, dp):
    if k == 0:
        return True
    if n == 0:
        return arr[0] == k
    if dp[n][k] is not None:
        return dp[n][k]
    pick = False
    if k >= arr[n]:
        pick = _is_subset_with_target(arr, n - 1, k - arr[n], dp)
    not_pick = _is_subset_with_target(arr, n - 1, k, dp)
    dp[n][k] = pick or not_pick
    return dp[n][k]


arr = [2, 3, 1, 1]
k = 4
print(is_subset_with_target(arr, k))


def is_subset_with_target_tabulation(arr, k):
    arr_len = len(arr)
    dp = [[False] * (k + 1) for _ in range(arr_len)]
    for row in range(len(dp)):
        dp[row][0] = True
    dp[0][arr[0]] = True
    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if arr[row] > col:
                dp[row][col] = False
            else:
                if arr[row] == col or dp[row - 1][col] or dp[row - 1][col - arr[row]]:
                    dp[row][col] = True
                else:
                    dp[row][col] = False
    for row in dp:
        print(row)
    return dp[arr_len - 1][k]


arr = [2, 3, 1, 1]
k = 4
print(is_subset_with_target_tabulation(arr, k))
