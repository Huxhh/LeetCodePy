# coding=utf-8

def generateMatrix(n):
    if not n:
        return []

    visited = [[False] * n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    di = r = c = 0
    res = [[0] * n for _ in range(n)]
    for i in range(n * n):
        nums = i + 1
        res[r][c] = nums
        visited[r][c] = True
        cr, cc = r + dr[di], c + dc[di]

        if 0 <= cr < n and 0 <= cc < n and not visited[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]

    return res


def generateMatrix2(n):
    if not n:
        return []

    res = [[0] * n for i in range(n)]
    l, r, t, b = 0, n - 1, 0, n - 1
    nums = 1
    maxs = n * n
    while nums <= maxs:
        for i in range(l, r + 1):
            res[t][i] = nums
            nums += 1
        t += 1
        for i in range(t, b + 1):
            res[i][r] = nums
            nums += 1
        r -= 1
        for i in range(r, l - 1, -1):
            res[b][i] = nums
            nums += 1
        b -= 1
        for i in range(b, t - 1, -1):
            res[i][l] = nums
            nums += 1
        l += 1

    return res


if __name__ == '__main__':
    n = 3
    print(generateMatrix2(n))
