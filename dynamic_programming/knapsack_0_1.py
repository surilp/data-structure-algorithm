def knapsack(weight, value, target):
    n = len(weight)
    return _knapsack(weight, value, target, n - 1)


def _knapsack(weight, value, target, n):
    if n == 0:
        if weight[n] <= target:
            return value[n]
        else:
            return 0
    # if weight[n] == target:
    #     return value[n]
    not_pick = _knapsack(weight, value, target, n - 1)
    pick = 0
    if weight[n] <= target:
        pick = value[n] + _knapsack(weight, value, target - weight[n], n - 1)
    return max(pick, not_pick)


def knapsack_tabulation(weight, value, target):
    n = len(weight)
    dp = [[0] * (target + 1) for _ in range(n)]
    for col in range(weight[0], target + 1):
        dp[0][col] = value[0]
    for n in range(1, len(dp)):
        for target in range(len(dp[0])):
            not_pick = dp[n - 1][target]
            pick = 0
            if weight[n] <= target:
                pick = value[n] + dp[n - 1][target - weight[n]]
            dp[n][target] = max(pick, not_pick)
    return dp[-1][-1]


weight = [3, 4, 5]
value = [30, 50, 60]
target = 8

print(knapsack(weight, value, target))
print(knapsack_tabulation(weight, value, target))

weight = [3, 2, 5]
value = [30, 40, 60]
target = 6

print(knapsack(weight, value, target))
