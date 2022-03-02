from collections import deque


def min_operation(start, end, arr):
    queue = deque()
    queue.append(start)
    visited = set()
    operation = 1
    while queue:
        size = len(queue)
        while size > 0:
            current = queue.popleft()
            for num in arr:
                temp = num * current
                if temp not in visited:
                    if temp < end:
                        queue.append(temp)
                        visited.add(temp)
                    elif temp == end:
                        return operation
            size -= 1
        operation += 1
    return -1


start = 3
end = 30
arr = [2, 5, 10]
print(min_operation(start, end, arr))

start = 2
end = 100
arr = [2, 5, 10]
print(min_operation(start, end, arr))
