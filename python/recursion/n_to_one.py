def print_n_to_one(n):
    if n > 0:
        print(n)
        print_n_to_one(n - 1)


print_n_to_one(10)

print('-' * 5)


def print_n_to_one_v2(n, i=1):
    if i <= n:
        print_n_to_one_v2(n, i + 1)
        print(i)


print_n_to_one_v2(10)
