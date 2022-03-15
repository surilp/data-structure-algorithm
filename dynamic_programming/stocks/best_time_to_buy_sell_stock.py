def best_time_to_buy(arr):
    max_profit = 0
    min_buy_price = arr[0]
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        min_buy_price = min(min_buy_price, temp)
        max_profit = max(max_profit, temp - min_buy_price)
    return max_profit


arr = [7, 1, 5, 3, 6, 4]
print(best_time_to_buy(arr))
