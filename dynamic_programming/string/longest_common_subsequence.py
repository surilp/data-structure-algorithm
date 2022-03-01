def longest_common_subsequence(string1, string2):
    string1_n = len(string1)
    string2_n = len(string2)
    dp = [[None] * string2_n for _ in range(string1_n)]
    return _longest_common_subsequence(string1, string2, string1_n - 1, string2_n - 1, dp)


def _longest_common_subsequence(string1, string2, string1_n, string2_n, dp):
    if string1_n < 0 or string2_n < 0:
        return 0
    if not dp[string1_n][string2_n]:
        if string1[string1_n] == string2[string2_n]:
            dp[string1_n][string2_n] = 1 + _longest_common_subsequence(string1, string2, string1_n - 1, string2_n - 1,
                                                                       dp)
        else:
            dp[string1_n][string2_n] = max(_longest_common_subsequence(string1, string2, string1_n - 1, string2_n, dp),
                                           _longest_common_subsequence(string1, string2, string1_n, string2_n - 1, dp))
    return dp[string1_n][string2_n]


def longest_common_sequence_tabulation(str1, str2):
    str1_n = len(str1)
    str2_n = len(str2)
    dp = [[0] * str2_n for _ in range(str1_n)]
    for col in range(len(dp[0])):
        if str1[0] == str2[col]:
            dp[0][col] = 1
        elif col > 0 and dp[0][col - 1] > 0:
            dp[0][col] = dp[0][col - 1]
    for row in range(len(dp)):
        if str1[row] == str2[0]:
            dp[row][0] = 1
        elif row > 0 and dp[row - 1][0] > 0:
            dp[row][0] = dp[row - 1][0]
    for string1_n in range(1, len(dp)):
        for string2_n in range(1, len(dp[0])):
            if str1[string1_n] == str2[string2_n]:
                dp[string1_n][string2_n] = 1 + dp[string1_n - 1][string2_n - 1]
            else:
                dp[string1_n][string2_n] = max(dp[string1_n - 1][string2_n], dp[string1_n][string2_n - 1])
    return dp[str1_n - 1][str2_n - 1]


str1 = 'abcde'
str2 = 'ace'

print(longest_common_subsequence(str1, str2))
print(longest_common_sequence_tabulation(str1, str2))

str1 = 'bacde'
str2 = 'ace'

print(longest_common_subsequence(str1, str2))
print(longest_common_sequence_tabulation(str1, str2))
