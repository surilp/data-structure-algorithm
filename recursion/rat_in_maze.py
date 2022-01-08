maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]


def rat_in_maze(maze):
    result = []
    visited = set()
    directions = {
        'D': [1, 0],
        'R': [0, 1],
        'L': [0, -1],
        'U': [-1, 0]
    }
    _rat_in_maze(maze, visited, directions, [], (0, 0), result)
    return result


def _rat_in_maze(maze, visited, directions, ds, current, result):
    if current[0] == len(maze) - 1 and current[1] == len(maze[0]) - 1:
        result.append(''.join(ds))
        return

    for letter, direction in directions.items():
        new_direction = (current[0] + direction[0], current[1] + direction[1])
        if 0 <= new_direction[0] < len(maze) and 0 <= new_direction[1] < len(
                maze[0]) and new_direction not in visited and maze[new_direction[0]][new_direction[1]] != 0:
            ds.append(letter)
            visited.add(new_direction)
            _rat_in_maze(maze, visited, directions, ds, new_direction, result)
            ds.pop()
            visited.remove(new_direction)


print(rat_in_maze(maze))
