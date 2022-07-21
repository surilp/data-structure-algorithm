from collections import namedtuple, deque
from typing import Deque

Node = namedtuple('Node', ['row', 'col'])


def can_reach_destination(maze, start, destination):
    row_len = len(maze)
    col_len = len(maze[0])
    queue = deque()
    queue.append(start)
    visited = [[False] * col_len for _ in range(row_len)]

    while queue:
        row, col = queue.popleft()
        visited[row][col] = True
        if destination[0] == row and destination[1] == col:
            return True
        for row_inc, col_inc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            row_n = row
            col_n = col
            while 0 <= row_n + row_inc < row_len and 0 <= col_n + col_inc < col_len and maze[row_n + row_inc][
                col_n + col_inc] == 0:
                row_n += row_inc
                col_n += col_inc
            if not visited[row_n][col_n]:
                visited[row_n][col_n] = True
                queue.append((row_n, col_n))
    return False


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

start = [0, 4]
destination = [4, 4]

print(can_reach_destination(maze, start, destination))
