def max_profit(prices, k):

    n = len(prices)

    def helper(idx, buy, total):
        if idx == n:
            return 0

        if total == 0:
            return 0

        if buy:
            profit1 = -prices[idx] + helper(idx + 1, 0, total)
            profit2 = helper(idx + 1, 1, total)
        else:
            profit1 = prices[idx] + helper(idx + 1, 1, total - 1)
            profit2 = helper(idx + 1, 0, total)

        return max(profit1, profit2)

    return helper(0, 1, k)


prices = [3, 2, 6, 5, 0, 3]
k = 2
print(max_profit(prices, k))
