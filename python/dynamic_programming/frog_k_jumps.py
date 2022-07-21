n = 6
energy = [30, 10, 60, 10, 60, 50]


# memoization

def frog_jump(n, energy, k):
    cache = [None] * n
    return _frog_jump(n - 1, energy, cache, k)


def _frog_jump(n, energy, cache, k):
    if n == 0:
        return 0
    if n == 1:
        return abs(energy[1] - energy[0])
    if cache[n]:
        print(f'cache hit cache[{n}]')
        return cache[n]

    result = float('inf')
    for jump in range(1, k + 1):
        if n - jump >= 0:
            current = _frog_jump(n - jump, energy, cache, k) + abs(energy[n] - energy[n - jump])
            result = min(result, current)

    cache[n] = result
    return cache[n]


print(frog_jump(n, energy, 5))