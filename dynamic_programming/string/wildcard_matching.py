
def wildcard_matching(s1, s2):
    s1_n = len(s1)
    s2_n = len(s2)

    def helper(i, j):
        if i < 0 and j < 0:
            return True
        if j < 0:
            while i >= 0 and s1[i] == '*':
                i -= 1
            return i < 0
        if i < 0:
            return False

        if s1[i] == s2[j] and s1[i] == '?':
            return helper(i - 1, j - 1)

        if s1[i] not in ['*', '?']:
            return False

        if s1[i] == '*':
            return helper(i, j - 1) or helper(i - 1, j - 1) or helper(i - 1, j)

    return helper(s1_n - 1, s2_n - 1)


s1 = "ab*cd"
s2 = "abdefcd"
print(wildcard_matching(s1, s2))


s1 = "a"
s2 = "aa"
print(wildcard_matching(s1, s2))


s1 = "?a"
s2 = "cb"
print(wildcard_matching(s1, s2))


s1 = "*"
s2 = "aa"
print(wildcard_matching(s1, s2))

s1 = "**abcd"
s2 = "abcd"
print(wildcard_matching(s1, s2))

s1 = "ab?d"
s2 = "abcc"
print(wildcard_matching(s1, s2))
