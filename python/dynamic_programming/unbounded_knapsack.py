def unbounded_knapsack(weight, value, target):
    n = len(weight)
    return _unbounded_knapsack(weight, value, target, n-1)

def _unbounded_knapsack(weight, value, target, n):
    if n == 0:
        return value[0] * (target // weight[0])


    not_pick = _unbounded_knapsack(weight, value, target, n-1)
    pick = -float('inf')
    if weight[n] <= target:
        pick = value[n] + _unbounded_knapsack(weight, value, target- weight[n], n)
    return max(not_pick, pick)


def unbounded_knapsack_tabulation(weight, value, target):
    n = len(weight)
    dp = [ [-float('inf')] * (target + 1) for _ in range(n)]
    for col in range(len(dp[0])):
        dp[0][col] = value[0] * (col // weight[0])
    for n in range(1, len(dp)):
        for target in range(len(dp[0])):
            not_pick = dp[n-1][target]
            pick = -float('inf')
            if weight[n] <= target:
                pick = value[n] + dp[n][target- weight[n]]
            dp[n][target] = max(not_pick, pick)
    return dp[-1][-1]     
    

weight = [2,4,6]
value = [5,11,13]
target = 10

print(unbounded_knapsack(weight, value, target))
print(unbounded_knapsack_tabulation(weight, value, target))

