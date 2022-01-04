from typing import List


def combination_sum(arr: [int], target: int, idx: int, ds: [int], result: [[int]]) -> None:
    if idx >= len(arr):
        if target == 0:
            result.append(ds.copy())
        return
    if target < 0:
        return

    ds.append(arr[idx])
    combination_sum(arr, target - arr[idx], idx, ds, result)
    ds.pop()
    combination_sum(arr, target, idx + 1, ds, result)


arr1 = [2, 3, 6, 7]
target = 7

result = []
combination_sum(arr1, target, 0, [], result)
print(result)



def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    result = []
    _combinationSum2(candidates, target, 0, [], result)
    return result


def _combinationSum2(candidates, target, idx, ds, result):
    if idx >= len(candidates):
        return
    if target == 0:
        result.append(list(ds))
        return
    for i in range(idx, len(candidates)):
        if i > idx and candidates[idx] == candidates[idx-1]:
            continue
        ds.append(candidates[i])
        _combinationSum2(candidates, target - candidates[i], i + 1, ds, result)
        ds.pop()



candidates = [10,1,2,7,6,1,5]
target = 8

print(combinationSum2(candidates, target))


