'''
first element greater than x
'''

def lower_bound_of_x(arr, x):
    left = 0
    right = len(arr) - 1

    result = - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] <= x:
            left = mid + 1
        elif arr[mid] > x:
            result = mid
            right = mid - 1

    return result

arr = [1,1,2,3,6,6,9,11]
x = 6

print(lower_bound_of_x(arr, x))
print(lower_bound_of_x(arr, 4))
print(lower_bound_of_x(arr, 5))
print(lower_bound_of_x(arr, 9))
