array = [12, 3, 1, 2, -6, 5, -8, 6]
target_sum = 0


def three_sum(array, target_sum):
    if len(array) < 3:
        return []
    result = []
    array = sorted(array)
    for idx1 in range(len(array) - 2):
        idx2 = idx1 + 1
        idx3 = len(array) - 1
        while idx2 < idx3:
            total = array[idx1] + array[idx2] + array[idx3]
            if total == target_sum:
                result.append([array[idx1], array[idx2], array[idx3]])
                idx2 += 1
                idx3 -= 1
            elif total > target_sum:
                idx3 -= 1
            else:
                idx2 += 1
    return result


print(three_sum(array, target_sum))


def three_sum_v2(array, target_sum):
    if len(array) < 3:
        return []
    result = []
    for left in range(len(array)):
        current_sum = target_sum - array[left]
        helper = set()
        for right in range(left + 1, len(array)):
            if current_sum - array[right] in helper:
                result.append([array[left], current_sum - array[right], array[right]])
            helper.add(array[right])
    return result

print(three_sum_v2(array, target_sum))
