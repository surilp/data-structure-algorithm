def longest_common_substring(str1, str2):
    s1_n = len(str1)
    s2_n = len(str2)
    return _helper(str1, str2, s1_n - 1, s2_n - 1)


def _helper(s1, s2, s1_n, s2_n):
    if s1_n < 0 or s2_n < 0:
        return 0

    count = 0
    while s1_n >= 0 and s2_n >= 0 and s1[s1_n] == s2[s2_n]:
        count += 1
        s1_n -= 1
        s2_n -= 1

    if s1_n < 0 or s2_n < 0:
        return count
    return max(count, _helper(s1, s2, s1_n - 1, s2_n), _helper(s1, s2, s1_n, s2_n - 1))




str1 = "abcjklp"
str2 = "acjkp"
print(longest_common_substring(str1, str2))


str1 = "abcd"
str2 = "abzd"
print(longest_common_substring(str1, str2))