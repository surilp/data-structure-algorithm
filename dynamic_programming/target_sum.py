def target_sum(arr, target):
    n = len(arr)
    return _target_sum(n - 1, target, arr)


def _target_sum(n, target, arr):
    if n == 0:
        if target - arr[n] == 0 or target + arr[n] == 0:
            return 1
        else:
            return 0
    positive = _target_sum(n - 1, target - arr[n], arr)
    negative = _target_sum(n - 1, target - (arr[n] * -1), arr)
    return positive + negative


arr = [1, 1, 1, 1, 1]
target = 3

print(target_sum(arr, target))

arr = [1, 2, 3, 1]
target = 3

print(target_sum(arr, target))
