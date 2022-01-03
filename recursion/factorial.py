def factorial_of_n(n):
    if n <= 0:
        return 1
    return n * factorial_of_n(n - 1)


print(factorial_of_n(5))


def factorial_of_n_v2(n, result=1):
    if n <= 0:
        return result
    return factorial_of_n_v2(n-1, result * n)

print(factorial_of_n_v2(5))
