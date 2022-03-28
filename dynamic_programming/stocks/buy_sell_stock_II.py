def max_profit(prices):
    n = len(prices)
    dp = [[None] * 2 for _ in range(n)]

    def helper(idx, buy):
        if idx >= n:
            return 0

        if dp[idx][buy]:
            return dp[idx][buy]

        if buy:
            profit1 = -prices[idx] + helper(idx + 1, False)
            profit2 = helper(idx + 1, True)
        else:
            profit1 = prices[idx] + helper(idx + 1, True)
            profit2 = helper(idx + 1, False)
        dp[idx][buy] = max(profit1, profit2)
        return dp[idx][buy]

    return helper(0, True)


def max_profit_tabulation(prices):
    n = len(prices)
    dp = [[0] * 2 for _ in range(n + 1)]

    for idx in range(n - 1, -1, -1):
        for buy in range(2):
            if buy:
                profit1 = -prices[idx] + dp[idx + 1][False]
                profit2 = dp[idx + 1][True]
            else:
                profit1 = prices[idx] + dp[idx + 1][True]
                profit2 = dp[idx + 1][False]
            dp[idx][buy] = max(profit1, profit2)
    return dp[0][-1]


prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
print(max_profit_tabulation(prices))

prices = [1, 2, 3, 4, 5]
print(max_profit(prices))
print(max_profit_tabulation(prices))

prices = [7, 6, 4, 3, 1]
print(max_profit(prices))
print(max_profit_tabulation(prices))
