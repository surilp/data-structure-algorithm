from collections import deque
from heapq import heappop, heappush, heapify


def shortest_destination(maze, start, destination):
    row_len = len(maze)
    col_len = len(maze[0])
    heap = []
    distance = [[float('inf')] * col_len for _ in range(row_len)]
    distance[start[0]][start[1]] = 0
    heappush(heap, (0, start))
    visited = set()
    visited.add((start[0], start[1]))
    while heap:
        dist, node = heappop(heap)
        row, col = node
        if row == destination[0] and col == destination[1]:
            return dist
        for row_inc, col_inc in [-1, 0], [0, 1], [1, 0], [0, -1]:
            new_row = row
            new_col = col
            temp_distance = 0
            while 0 <= new_row + row_inc <row_len and 0 <= new_col + col_inc < col_len and maze[new_row + row_inc][new_col + col_inc] == 0:
                new_row = new_row + row_inc
                new_col = new_col + col_inc
                temp_distance += 1
            new_dist = temp_distance + dist
            if (new_row, new_col) not in visited and distance[new_row][new_col] > new_dist:
                distance[new_row][new_col] = new_dist
                heappush(heap, (new_dist, (new_row, new_col)))
    return -1



maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

start = [0, 4]
destination = [4, 4]

print(shortest_destination(maze, start, destination))


maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

start = [0, 4]
destination = [0, 0]

print(shortest_destination(maze, start, destination))