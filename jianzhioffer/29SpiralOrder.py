# coding=utf-8
# author huxh
# time 2020/3/26 10:24 AM


# O(MN) O(MN)
def spiralOrder(matrix):
    if not matrix:
        return []
    visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]

    res = []
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    di = 0
    i, j = 0, 0
    r = len(matrix)
    c = len(matrix[0])
    for _ in range(r * c):
        visited[i][j] = 1
        res.append(matrix[i][j])
        ni, nj = i + d[di][0], j + d[di][1]
        if not 0 <= ni < r or not 0 <= nj < c or visited[ni][nj]:
            di = (di + 1) % 4
            i, j = i + d[di][0], j + d[di][1]
        else:
            i, j = i + d[di][0], j + d[di][1]
    return res


# O(MN) O(1)
def spiralOrder2(matrix):
    if not matrix:
        return []

    l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
    while 1:
        for i in range(l, r + 1):
            res.append(matrix[t][i])
        t += 1
        if t > b:
            break
        for i in range(t, b + 1):
            res.append(matrix[i][r])
        r -= 1
        if r < l:
            break
        for i in range(r, l - 1, -1):
            res.append(matrix[b][i])
        b -= 1
        if b < t:
            break
        for i in range(b, t - 1, -1):
            res.append(matrix[i][l])
        l += 1
        if l > r:
            break
    return res