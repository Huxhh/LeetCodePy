# coding=utf-8
# author huxh
# time 2020/3/25 9:51 AM

def surfaceArea(grid):
    if not grid:
        return 0

    n = len(grid)
    res = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                res += 2

                for r , c in ((i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)):
                    if 0 <= r < n and 0 <= c < n:
                        val = grid[r][c]
                    else:
                        val = 0

                    res += max(grid[i][j] - val, 0)
    return res

