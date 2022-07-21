

def rod_cutting(n, price):
    dp = [[None] * (n + 1) for _ in range(len(price)) ]
    return _rod_cutting(n-1, price, n, dp)

def _rod_cutting(n, price, length, dp):
    if n == 0:
        return length * price[n]

    if dp[n][length]:
        return dp[n][length]

    not_pick = _rod_cutting(n - 1, price, length, dp)
    pick = -float('inf')
    if n + 1 <= length:
        pick = price[n] + _rod_cutting(n, price, length - (n + 1), dp)

    dp[n][length] = max(not_pick, pick)
    return dp[n][length]


def rod_cutting_tabulation(n, price):
    dp = [[None] * (n + 1) for _ in range(len(price)) ]
    for target in range(len(dp[0])):
        dp[0][target] = target * price[0]
    for n in range(1, len(dp)):
        for length in range(len(dp[0])):
            not_pick = dp[n - 1][length]
            pick = -float('inf')
            if n + 1 <= length:
                pick = price[n] + dp[n][length - (n + 1)]

            dp[n][length] = max(not_pick, pick)
    return dp[-1][-1]


price = [2, 5, 7, 8, 10]
n = 5

print(rod_cutting(n, price))
print(rod_cutting_tabulation(n, price))
