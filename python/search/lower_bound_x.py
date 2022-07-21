'''
first element greater than equal to x
'''

def lower_bound_of_x(arr, x):
    left = 0
    right = len(arr) - 1

    result = - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= x:
            result = mid
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1

    return result

arr = [1,3,4,6,7,8,8,10,12,13]
x = 5

print(lower_bound_of_x(arr, x))
print(lower_bound_of_x(arr, 11))
