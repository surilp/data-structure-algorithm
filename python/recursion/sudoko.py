from typing import Set, List, Dict, Tuple

board = [
    [5, 3, -1, 6, 7, 8, 9, -1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [-1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, -1, 4, 8, 5, 6],
    [9, 6, -1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


def sudoko(board):
    row_hash, col_hash, box_hash = get_hashes(board)
    _sudoko(0, 0, board, row_hash, col_hash, box_hash)
    return board


def _sudoko(row, col, board, row_hash, col_hash, box_hash):
    if row == len(board):
        return True

    if board[row][col] == -1:
        for num in range(1, 10):
            if num not in row_hash[row] and num not in col_hash[col] and num not in box_hash[(row // 3, col // 3)]:
                board[row][col] = num
                row_hash[row].add(num)
                col_hash[col].add(num)
                box_hash[(row // 3, col // 3)].add(num)
                if col == len(board[0]) - 1:
                    if _sudoko(row + 1, 0, board, row_hash, col_hash, box_hash):
                        return True
                else:
                    if _sudoko(row, col + 1, board, row_hash, col_hash, box_hash):
                        return True
                board[row][col] = -1
                row_hash[row].remove(num)
                col_hash[col].remove(num)
                box_hash[(row // 3, col // 3)].remove(num)
        return False

    else:
        if col == len(board[0]) - 1:
            return _sudoko(row + 1, 0, board, row_hash, col_hash, box_hash)
        else:
            return _sudoko(row, col + 1, board, row_hash, col_hash, box_hash)


def get_hashes(board):
    row_hash: List[Set] = [set() for _ in range(len(board))]
    col_hash: List[Set] = [set() for _ in range(len(board[0]))]
    box_hash: Dict[Tuple, Set] = {}
    for row_idx, row in enumerate(board):
        for col_idx, num in enumerate(board[row_idx]):
            if num != - 1:
                row_hash[row_idx].add(num)
                col_hash[col_idx].add(num)
                grid_row = row_idx // 3
                grid_col = col_idx // 3
                if (grid_row, grid_col) in box_hash:
                    box_hash[(grid_row, grid_col)].add(num)
                else:
                    box_hash[(grid_row, grid_col)] = {num}
    return row_hash, col_hash, box_hash


print(sudoko(board))
