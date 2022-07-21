
def func(array, k):
    n = len(array)
    result = []
    for i in range(n):
        result.append([array[i]])
        for j in range(i + 1, n):
            temp = []
            for k in range(i, j + 1):
                temp.append(array[k])
            result.append(temp)
    count = 0
    for item in result:
        result = 0
        for ele in item:
            result = result ^ ele
        if result == k:
            count += 1
    return count




array = [4,2,2,6,4]
k = 6

print(func(array, k))