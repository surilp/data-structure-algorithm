from pprint import pprint


def sub_set_count(arr, target):
    arr_len = len(arr)
    dp = [[None] * (target + 1) for _ in range(arr_len)]
    result = _sub_set_count(arr, arr_len - 1, target, dp)
    pprint(result)


def _sub_set_count(arr, n, target, dp):
    if target == 0:
        return 1
    if n == 0:
        if arr[0] == target:
            return 1
        else:
            return 0
    if dp[n][target]:
        return dp[n][target]
    not_pick = _sub_set_count(arr, n - 1, target, dp)
    pick = 0
    if arr[n] <= target:
        pick = _sub_set_count(arr, n - 1, target - arr[n], dp)
    dp[n][target] = not_pick + pick
    return dp[n][target]


def sub_set_tabulation(arr, target):
    arr_len = len(arr)
    dp = [[0] * (target + 1) for _ in range(arr_len)]
    for n in range(arr_len):
        dp[n][0] = 1
    if arr[0] <= target:
        dp[0][arr[0]] = 1

    for n in range(1, arr_len):
        for target in range(1, len(dp[0])):
            not_pick = dp[n - 1][target]
            pick = 0
            if arr[n] <= target:
                pick = dp[n - 1][target - arr[n]]
            dp[n][target] = not_pick + pick
    pprint(dp)
    return dp[arr_len - 1][target]

    pprint(dp)


arr = [1, 2, 2, 3]
target = 3

print(sub_set_count(arr, 3))
print(sub_set_tabulation(arr, 3))
