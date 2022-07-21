'''
1) index
2) do all stuff on that index
3) take the min
'''

n = 6
energy = [30, 10, 60, 10, 60, 50]


# memoization

def frog_jump(n, energy):
    cache = [None] * n
    return _frog_jump(n - 1, energy, cache)


def _frog_jump(n, energy, cache):
    if n == 0:
        return 0
    if n == 1:
        return abs(energy[1] - energy[0])
    if cache[n]:
        print(f'cache hit cache[{n}]')
        return cache[n]
    one = _frog_jump(n - 1, energy, cache) + abs(energy[n] - energy[n - 1])
    two = _frog_jump(n - 2, energy, cache) + abs(energy[n] - energy[n - 2])
    cache[n] = min(one, two)
    return cache[n]


print(frog_jump(n, energy))


# tabulation

def frog_jump_v2(n, energy):
    cache = [None] * n
    return _frog_jump_v2(n, energy, cache)


def _frog_jump_v2(n, energy, cache):
    cache[0] = 0
    cache[1] = abs(energy[1] - energy[0])
    for idx in range(2, n):
        cache[idx] = min(cache[idx - 1] + abs(energy[idx] - energy[idx - 1]),
                         cache[idx - 2] + abs(energy[idx] - energy[idx - 2]))
    return cache[n - 1]


print(frog_jump_v2(n, energy))


# optimized

def frog_jump_v3(n, energy):
    if n == 1:
        return 0
    if n == 2:
        return abs(energy[1] - energy[0])
    return _frog_jump_v3(n, energy)


def _frog_jump_v3(n, energy):
    prev = 0
    current = abs(energy[1] - energy[0])
    for idx in range(2, n):
        prev, current = current, min(current + abs(energy[idx] - energy[idx - 1]),
                                     prev + abs(energy[idx] - energy[idx - 2]))
    return current


print(frog_jump_v3(n, energy))
