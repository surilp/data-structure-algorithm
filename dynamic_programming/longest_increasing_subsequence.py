nums = [10, 9, 2, 5, 3, 7, 101, 18]


def subsequence(nums):
    return _subsequence(nums, [], 0)


def _subsequence(nums, ds, idx):
    if idx == len(nums):
        return len(ds)

    result = -float('inf')
    if not ds or nums[idx] > ds[-1]:
        ds.append(nums[idx])
        result = max(_subsequence(nums, ds, idx + 1),result)
        ds.pop()
    result = max(_subsequence(nums, ds, idx + 1), result)
    return result


print(subsequence(nums))