def longestConsecutive(nums) -> int:
    hash_set = set(nums)
    result = 0
    for num in nums:
        count = 1
        if num - 1 not in hash_set:
            temp = num + 1
            while temp in hash_set:
                count += 1
                temp = num + 1
            result = max(result, count)
    return result


longestConsecutive([100, 4, 200, 1, 3, 2])
