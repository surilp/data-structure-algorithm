def subset_sum_1(arr: [int]) -> [int]:
    result = []
    _subset_num_1(arr, 0, 0, result)
    result.sort()
    return result



def _subset_num_1(arr: [int], idx: int, total:int, result: [int]) -> None:
    if idx >= len(arr):
        result.append(total)
        return
    _subset_num_1(arr, idx + 1, total + arr[idx], result)
    _subset_num_1(arr, idx + 1, total, result)


arr = [3, 1, 2]
print(subset_sum_1(arr))


def unique_subsets(nums: [int]) -> [[int]]:
    result = []
    _unique_subsets(nums, 0, [], result)
    return result

def _unique_subsets(nums: [int], idx: int, ds: [int], result: [[int]]):
    if idx <= len(nums):
        result.append(list(ds))

    if idx >= len(nums):
        return

    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]:
            continue
        ds.append(nums[i])
        _unique_subsets(nums, i +1, ds, result)
        ds.pop()

print(unique_subsets([1,2,2,2,3,3]))
