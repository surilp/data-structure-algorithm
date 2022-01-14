board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"],
]

words = [
    "this", "is", "not", "a", "simple", "boggle",
    "board", "test", "REPEATED", "NOTRE-PEATED",
]


def boggle_board(board, words):
    result = []
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for word in words:
        visited = set()
        for row_idx in range(len(board)):
            for col_idx in range(len(board[row_idx])):
                if _is_word_in_board(board, word, visited, directions, (row_idx, col_idx), 0):
                    result.append(word)
                    break
            else:
                continue
            break
    return result


def _is_word_in_board(board, word, visited, directions, current_idx, word_idx):
    current_row_idx, current_col_idx = current_idx
    if word[word_idx] == board[current_row_idx][current_col_idx]:
        if word_idx == len(word) - 1:
            return True
        visited.add((current_row_idx, current_col_idx))
        for row_inc, col_inc in directions:
            new_row_idx, new_col_idx = current_row_idx + row_inc, current_col_idx + col_inc
            if 0 <= new_row_idx < len(board) and 0 <= new_col_idx < len(board[0]) and (
                    new_row_idx, new_col_idx) not in visited:
                if _is_word_in_board(board, word, visited, directions, (new_row_idx, new_col_idx), word_idx + 1):
                    return True

        visited.remove((current_row_idx, current_col_idx))
    return False


boggle_board(board, words)
