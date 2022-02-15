
def int_sqrt(n):
    result = 1
    left = 1
    right = n

    while left <= right:
        mid = (left + right)//2
        cur = mid * mid
        if cur ==  n:
            return mid
        if cur > n:
            right = mid - 1
        else:
            result = mid
            left = mid + 1
    return result


print(int_sqrt(26))