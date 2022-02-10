def min_coin(coins, target):
    n = len(coins)
    return _min_coin(coins, target, n - 1)


def _min_coin(coins, target, n):
    if n == 0:
        if target % coins[n] == 0:
            return target // coins[n]
        return float('inf')
    if target == 0:
        return 0
    # if target == coins[n]:
    #     return 1
    pick = float('inf')
    if coins[n] <= target:
        pick = 1 + _min_coin(coins, target - coins[n], n)
    not_pick = _min_coin(coins, target, n - 1)
    return min(pick, not_pick)


def min_coin_tabulation(coins, target):
    n = len(coins)
    dp = [[-float('inf')] * (target + 1) for _ in range(n)]
    for tar in range(target + 1):
        if tar % coins[0] == 0:
            dp[0][tar] = tar // coins[0]
    for n in range(1, len(dp)):
        for target in range(len(dp[0])):
            pick = float('inf')
            if coins[n] <= target:
                pick = 1 + dp[n][target - coins[n]]
            not_pick = dp[n-1][target]
            dp[n][target] = min(pick, not_pick)
    return dp[-1][-1]


coins = [1, 2, 3]
target = 8
print(min_coin(coins, target))
print(min_coin_tabulation(coins, target))

coins = [1, 6, 5, 9]
target = 11
print(min_coin(coins, target))
print(min_coin_tabulation(coins, target))
