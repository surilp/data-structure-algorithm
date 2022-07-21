def num_of_occurence(arr, x):
    first = first_occurence(arr, x)
    last = last_occurence(arr, x)
    return last- first + 1

def first_occurence(arr, x):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            right = mid - 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return result

def last_occurence(arr, x):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid
            left = mid + 1
        elif x > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return result


x = 7
arr = [1,3,5,7,7,7,10]
print(num_of_occurence(arr, x))