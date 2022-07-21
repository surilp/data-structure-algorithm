def zigzagTraverse(array):
    row_len = len(array)
    col_len = len(array[0])

    dr = [-1, 1]
    dl = [1, -1]

    is_dr = False

    row = 0
    col = 0

    result = []
    while row < row_len or col < col_len:
        result.append(array[row][col])
        if row == row_len - 1 and col == col_len - 1:
            break
        if is_dr:
            row = row + dr[0]
            col = col + dr[1]
        else:
            row = row + dl[0]
            col = col + dl[1]
        if col >= col_len:
            col -= 1
            row += 2
            is_dr = False
        elif row >= row_len:
            row -= 1
            col += 2
            is_dr = True
        elif col < 0:
            col = 0
            is_dr = True
        elif row < 0:
            row = 0
            is_dr = False
    return result


array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16],
]

print(zigzagTraverse(array))
