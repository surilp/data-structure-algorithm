'''
backtracking

generate all possible ways

recursive func(args, ans)
loop over possible value
 push current value
 decide if it is valid
 if valid recusivly call func(args, ans)

 remove current value from ans

'''


def nqueen(n):
    board = [['.'] * n for _ in range(n)]
    queen_locations = set()
    result = []
    _nqueen(0, board, queen_locations, result)
    return result


def _nqueen(col, board, queen_locations, result):
    if col == len(board[0]):
        temp = [row.copy() for row in board]
        result.append(temp)
        return

    for row in range(len(board)):
        board[row][col] = "Q"
        if not can_attack((row, col), queen_locations):
            queen_locations.add((row, col))
            _nqueen(col + 1, board, queen_locations, result)
            queen_locations.remove((row, col))
        board[row][col] = "."


def can_attack(potential_queen_location, queen_locations):
    potential_queen_row, potential_queen_col = potential_queen_location
    for queen_row, queen_col in queen_locations:
        if queen_row == potential_queen_row or queen_col == potential_queen_col:
            return True
        if abs(potential_queen_row - queen_row) == abs(potential_queen_col - queen_col):
            return True
    return False


assert can_attack((0, 0), {}) == False, "Test failed"
assert can_attack((0, 0), {(0, 4)}) == True, "Test failed"
assert can_attack((0, 0), {(4, 4)}) == True, "Test failed"
assert can_attack((0, 0), {(4, 0)}) == True, "Test failed"
assert can_attack((0, 0), {(1, 2)}) == False, "Test failed"


def print_board(board):
    print('-' * 10)
    for row in board:
        print(row)
    print('-' * 10)


for board in nqueen(4):
    print(print_board(board))
