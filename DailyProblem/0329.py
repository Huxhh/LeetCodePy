# coding=utf-8
# author huxh
# time 2020/3/29 9:58 AM


def maxDistance(grid):
    if not grid:
        return 0

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = -1
    q = []
    rows = len(grid)
    cols = len(grid[0])
    vis = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                vis[i][j] = 1
                q.append((i, j, -1))

    while q:
        x, y, dis = q.pop(0)
        res = max(res, dis)
        for di in d:
            ni = x + di[0]
            nj = y + di[1]
            if 0 <= ni < rows and 0 <= nj < cols and not grid[ni][nj] and not vis[ni][nj]:
                vis[ni][nj] = 1
                q.append((ni, nj, dis + 1))

    return res + 1 if res >= 0 else -1


if __name__ == '__main__':
    print(maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
