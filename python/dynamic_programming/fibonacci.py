# memoization - answer -> base case

def fibonnaci(n):
    cache = [-1] * (n + 1)
    return _fibonnaci(n, cache)


def _fibonnaci(n, cache):
    if n <= 1:
        return n
    if cache[n] != -1:
        return cache[n]
    cache[n] = _fibonnaci(n - 1, cache) + _fibonnaci(n - 2, cache)
    return cache[n]


print(fibonnaci(5))


# tabulation - base case to the required

def fibonnaci_v2(n):
    cache = [-1] * (n + 1)
    cache[0] = 0
    cache[1] = 1
    for idx in range(2, n + 1):
        cache[idx] = cache[idx - 1] + cache[idx - 2]
    return cache[n]


print(fibonnaci_v2(50000))


# constant space

def fibonnaci_v3(n):
    if n <= 1:
        return n
    cache = [0, 1]
    for idx in range(2, n + 1):
        cache[0], cache[1] = cache[1], cache[0] + cache[1]
    return cache[1]


print(fibonnaci_v3(50000))

