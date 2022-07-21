
def buy_sell_stock_with_fee(prices, fee):
    n = len(prices)

    def helper(idx, buy):
        if idx >= n:
            return 0

        if buy:
            profit1 = -prices[idx] + helper(idx + 1, 0)
            profit2 = helper(idx + 1, 1)
        else:
            profit1 = prices[idx] + helper(idx + 1, 1) - fee
            profit2 = helper(idx + 1, 0)

        return max(profit1, profit2)

    return helper(0, 1)


prices = [1, 3, 2, 8, 4, 9]
fee = 2
print(buy_sell_stock_with_fee(prices, fee))
