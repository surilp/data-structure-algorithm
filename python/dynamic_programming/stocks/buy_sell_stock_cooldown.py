def buy_sell_with_cooldown(prices):
    n = len(prices)

    def helper(idx, buy):
        if idx >= n:
            return 0

        if buy:
            profit1 = -prices[idx] + helper(idx + 1, 0)
            profit2 = helper(idx + 1, 1)
        else:
            profit1 = prices[idx] + helper(idx + 2, 1)
            profit2 = helper(idx + 1, 0)

        return max(profit1, profit2)

    return helper(0, 1)


prices = [4, 9, 0, 4, 10]
print(buy_sell_with_cooldown(prices))
