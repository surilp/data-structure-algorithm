
def sum_of_first_n(n):
    if n > 0:
        return n + sum_of_first_n(n-1)
    return 0

print(sum_of_first_n(3))

def sum_of_first_n_v2(n, sum):
    if n <= 0:
        return sum
    return sum_of_first_n_v2(n-1, sum + n)

print(sum_of_first_n_v2(3, 0))