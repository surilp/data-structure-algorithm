def inversion_count(nums):
    n = len(nums)
    global_inversion_count = calculate_global_inversion_count(nums, 0, n - 1)
    return global_inversion_count


def calculate_global_inversion_count(nums, start, end):
    if start == end:
        return 0
    mid = (start + end) // 2
    left = calculate_global_inversion_count(nums, start, mid)
    right = calculate_global_inversion_count(nums, mid + 1, end)
    c_left = start
    c_right = mid + 1
    count = 0
    while c_left <= mid and c_right <= end:
        if nums[c_right] < nums[c_left]:
            count += mid - c_left + 1
            c_right += 1
        else:
            c_left += 1
    c_left = start
    c_right = mid + 1
    while c_left <= mid and c_right <= end:
        if nums[c_right] < nums[c_left]:
            nums[c_right], nums[c_left] = nums[c_left], nums[c_right]
            i = c_right
            while i < end:
                if nums[i] < nums[i + 1]:
                    break
                else:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    i += 1
        c_left += 1
    return count + left + right


print(inversion_count([5, 3, 2, 4, 1]))
