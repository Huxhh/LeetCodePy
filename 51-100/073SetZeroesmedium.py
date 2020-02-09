# coding=utf-8


def setZeroes(matrix):
    if not matrix:
        return matrix

    rows = len(matrix)
    cols = len(matrix[0])
    is_col = False

    for i in range(rows):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # for i in range(1, rows):
    #     if matrix[i][0] == 0:
    #         for j in range(1, cols):
    #             matrix[i][j] = 0
    #
    # for i in range(1, cols):
    #     if matrix[0][i] == 0:
    #         for j in range(1, rows):
    #             matrix[j][i] = 0

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if matrix[0][0] == 0:
        for i in range(cols):
            matrix[0][i] = 0

    if is_col:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


if __name__ == '__main__':
    matrix = [
  [1,1,1],
  [0,1,2]
]
    print(setZeroes(matrix))
