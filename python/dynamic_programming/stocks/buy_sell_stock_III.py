def max_profit_2_transactions(prices):
    n = len(prices)

    dp = []
    for idx in range(n):
        temp = [[None, None, None], [None, None, None]]
        dp.append(temp)

    def helper(idx, buy, total):
        if total <= 0:
            return 0

        if idx >= n:
            return 0

        if dp[idx][buy][total]:
            return dp[idx][buy][total]
        profit1 = 0
        profit2 = 0
        if buy:
            profit1 = -prices[idx] + helper(idx + 1, 0, total)
            profit2 = helper(idx + 1, 1, total)
        else:
            profit1 = prices[idx] + helper(idx + 1, 1, total - 1)
            profit2 = helper(idx + 1, 0, total)

        dp[idx][buy][total] = max(profit1, profit2)
        return dp[idx][buy][total]

    return helper(0, 1, 2)


prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(max_profit_2_transactions(prices))
