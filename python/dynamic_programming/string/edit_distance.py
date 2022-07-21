def edit_distance(s1, s2):
    s1_n = len(s1)
    s2_n = len(s2)

    def helper(i, j):
        if j < 0:
            return i + 1
        if i < 0:
            return j + 1

        if s1[i] == s2[j]:
            return helper(i - 1, j - 1)
        else:
            replace = 1 + helper(i - 1, j - 1)
            insert = 1 + helper(i, j - 1)
            delete = 1 + helper(i - 1, j)
            return min(replace, delete, insert)

    return helper(s1_n - 1, s2_n - 1)


s1 = "horse"
s2 = "ros"
print(edit_distance(s1, s2))

s1 = "intention"
s2 = "execution"
print(edit_distance(s1, s2))
