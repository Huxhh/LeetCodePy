# coding=utf-8


def spiralOrder(matrix):
    if not matrix:
        return []

    res = []
    rows = len(matrix)
    cols = len(matrix[0])

    def right(begin, end, mt, crow):
        tmp = []
        for i in range(begin, end):
            tmp.append(mt[crow][i])
        return tmp

    def down(begin, end, mt, ccol):
        tmp = []
        for i in range(begin, end):
            tmp.append(mt[i][ccol])
        return tmp

    def up(begin, end, mt, ccol):
        tmp = []
        for i in range(begin, end, -1):
            tmp.append(mt[i][ccol])
        return tmp

    def left(begin, end, mt, crow):
        tmp = []
        for i in range(begin, end, -1):
            tmp.append(mt[crow][i])
        return tmp

    for i in range(rows // 2 + rows % 2):
        if i * 2 < rows and i * 2 < cols:
            res += right(i, cols - i, matrix, i)
            # print(right(i, cols - i, matrix, i))
            res += down(i + 1, rows - i, matrix, cols - 1 - i)
            # print(down(i + 1, rows - i, matrix, cols - 1 - i))
            if rows - 1 - i > i and cols - 1 - i > i:
                res += left(cols - 2 - i, i, matrix, rows - 1 - i)
                # print(left(cols - 2 - i, i, matrix, rows - 1 - i))
                res += up(rows - 1 - i, i, matrix, i)
                # print(up(rows - 1 - i, i, matrix, i))

    return res


def spiralOrder2(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    res = []
    for i in range(rows * cols):
        visited[r][c] = True
        res.append(matrix[r][c])
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < rows and 0 <= cc < cols and not visited[cr][cc]:
            c, r = cc, cr
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]

    return res


if __name__ == '__main__':
#     matrix = [
#   [1, 2, 3, 4, 13],
#   [5, 6, 7, 8, 14],
#   [9,10,11,12, 15],
#   [16,17,18,19,20]
# ]
    matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]

    print(spiralOrder2(matrix))

