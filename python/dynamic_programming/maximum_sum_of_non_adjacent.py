from functools import lru_cache

nums = [2, 1, 4, 9]


def maximum_sum_of_non_adjacent(nums):
    cache = [None] * len(nums)
    return _maximum_sum_of_non_adjacent(tuple(nums), len(nums) - 1, cache)


def _maximum_sum_of_non_adjacent(nums, n, cache):
    if n == 0:
        return nums[n]
    if n == 1:
        return max(nums[0], nums[1])
    if cache[n]:
        return cache[n]
    cache[n] = max(_maximum_sum_of_non_adjacent(nums, n - 2, cache) + nums[n],
                   _maximum_sum_of_non_adjacent(nums, n - 1, cache))
    return cache[n]


print(maximum_sum_of_non_adjacent(nums))


def maximum_sum_of_non_adjacent_v2(nums):
    cache = [None] * len(nums)
    return _maximum_sum_of_non_adjacent_v2(nums, cache)


def _maximum_sum_of_non_adjacent_v2(nums, cache):
    cache[0] = nums[0]
    cache[1] = max(nums[0], nums[1])
    for idx in range(2, len(nums)):
        cache[idx] = max(cache[idx - 1], cache[idx - 2] + nums[idx])
    return cache[len(nums) - 1]


print(maximum_sum_of_non_adjacent_v2(nums))


def maximum_sum_of_non_adjacent_v3(nums):
    return _maximum_sum_of_non_adjacent_v3(nums)


def _maximum_sum_of_non_adjacent_v3(nums):
    prev = nums[0]
    current = max(nums[0], nums[1])
    for idx in range(2, len(nums)):
        prev, current = current, max(current, prev + nums[idx])
    return current


print(maximum_sum_of_non_adjacent_v3(nums))
