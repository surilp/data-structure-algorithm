from array import array


def ways_to_make_coin_change(coins, target):
    n = len(coins)
    return _ways_to_make_coin_change(coins, target, n-1)

def _ways_to_make_coin_change(coins, target, n):
    if n == 0:
        if target % coins[n] == 0:
            return 1
        else:
            return 0
    if target == 0:
        return 1
    not_pick = _ways_to_make_coin_change(coins, target, n-1)
    pick = 0
    if coins[n] <= target:
        pick = _ways_to_make_coin_change(coins, target - coins[n], n)
    return not_pick + pick

def ways_to_make_coin_change_tabulation(coins, target):
    dp = [[0] * (target + 1) for _ in range(len(coins))]
    # for row in range(len(dp)):
    #     dp[row][0] = 1
    for col in range(len(dp[0])):
        if col % coins[0] == 0:
            dp[0][col] = 1
    
    for n in range(1, len(dp)):
        for target in range(len(dp[0])):
            not_pick = dp[n-1][target]
            pick = 0
            if coins[n] <= target:
                pick = dp[n][target - coins[n]]
            dp[n][target] = not_pick + pick
    return dp[-1][-1]


arr = [1,2,3]
target = 4

print(ways_to_make_coin_change(arr, target))
print(ways_to_make_coin_change_tabulation(arr, target))
