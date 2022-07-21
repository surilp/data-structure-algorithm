from math import factorial
from itertools import permutations


def kth_perm(n, k):
    arr = [num for num in range(1, n+1)]
    return _kth_perm(arr, k - 1, [])


def _kth_perm(arr, k, ds):

    if not arr:
        return ds

    fact = factorial(len(arr))
    group = fact // len(arr)
    div = k // group
    mod = k % group
    print(k, ds, fact, group, div, mod)
    ds.append(arr[div])
    return _kth_perm(arr[:div] + arr[div + 1:], mod, ds)



print(kth_perm(4, 9))



for i, num in  enumerate(permutations(range(1,5)), start = 1):
    print(i, num)