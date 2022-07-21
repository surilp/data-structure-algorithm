'''
1) start with entire block | array (represent with i and j)
2) Try all partition - run a loop to try all partitions
3) Return the best possible 2 partitions

'''


def func(arr):
    n = len(arr)
    dp = [[None] * n for _ in range(n)]
    return _func(arr, 1, len(arr) - 1, dp)


def _func(arr, start, end, dp):
    if start == end:
        return 0

    if not dp[start][end]:
        result = float('inf')
        for mid in range(start, end):
            cur = (arr[start - 1] * arr[mid] * arr[end]) + _func(arr, start, mid, dp) + _func(arr, mid + 1, end, dp)
            result = min(cur, result)
    dp[start][end] = result
    return dp[start][end]


def tabulation(arr):
    n = len(arr)
    dp = [[None] * n for _ in range(n)]

    for idx in range(n):
        dp[idx][idx] = 0

    for i in range(n - 1, 0, -1):
        for j in range(i + 1 , n):
            result = float('inf')
            for k in range(i, j):
                cur = (arr[i - 1] * arr[k] * arr[j]) + dp[i][k] + dp[k+1][j]
                result = min(cur, result)
            dp[i][j] = result
    return dp[1][-1]


arr = [4, 5, 3, 2]
print(func(arr))
print(tabulation(arr))

arr = [1, 4, 3, 2]
print(func(arr))
print(tabulation(arr))