from collections import deque
from random import shuffle


def minOperations(arr):
    current = ''.join(list(map(str, arr)))
    destination = ''.join(sorted(current))
    visited = set()
    queue = deque()
    queue.append(current)
    visited.add(current)
    result = 0
    while queue:
        size = len(queue)
        while size > 0:
            current = queue.popleft()
            if current == destination:
                return result
            for idx in range(len(arr)):
                new_perm = current[:idx + 1][::-1] + current[idx + 1:]
                if new_perm not in visited:
                    queue.append(new_perm)
                new_perm = current[:idx + 1] + current[idx + 1:][::-1]
                if new_perm not in visited:
                    queue.append(new_perm)
            size -= 1
        result += 1


print(minOperations([3, 1, 2]))
print(minOperations([1, 2, 5, 4, 3]))