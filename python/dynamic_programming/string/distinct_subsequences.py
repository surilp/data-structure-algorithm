def distinct_subsequences(s1, s2):
    s1_n = len(s1)
    s2_n = len(s2)

    if s1_n < s2_n:
        s1, s2 = s2, s1
        s1_n, s2_n = s2_n, s1_n
    elif s1_n == s2_n:
        return 1 if s1 == s2 else 0

    dp = [[None] * s2_n for _ in range(s1_n)]

    return helper(s1, s2, s1_n - 1, s2_n - 1, dp)


def helper(s1, s2, i, j, dp):
    if j < 0:
        return 1
    if i < 0:
        return 0

    if dp[i][j]:
        return dp[i][j]

    not_pick = helper(s1, s2, i - 1, j, dp)
    pick = 0
    if s1[i] == s2[j]:
        pick = helper(s1, s2, i - 1, j - 1, dp)
    dp[i][j] = not_pick + pick
    return dp[i][j]


s1 = "bag"
s2 = "babgbag"
print(distinct_subsequences(s1, s2))


s1 = "rabbbit"
s2 = "rabbit"
print(distinct_subsequences(s1, s2))


s1 = "fff"
s2 = "ffff"
print(distinct_subsequences(s1, s2))
