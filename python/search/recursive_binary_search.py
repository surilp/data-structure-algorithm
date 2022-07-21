def binary_search(arr, target):
    return _binary_search(arr, target, 0, len(arr) - 1)

def _binary_search(arr, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end)//2

    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return _binary_search(arr, target, mid + 1, end)
    else:
        return _binary_search(arr, target, start, mid - 1)


arr = [1,3,4,5,8,10,12,15,16,17,18]
target = 8

print(binary_search(arr, target))