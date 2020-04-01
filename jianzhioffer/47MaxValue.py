# coding=utf-8
# author huxh
# time 2020/4/1 11:39 PM


def maxValue(grid):
    if not grid:
        return 0

    for i in range(1, len(grid)):
        grid[i][0] += grid[i - 1][0]

    for i in range(1, len(grid[0])):
        grid[0][i] += grid[0][i - 1]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
    return grid[-1][-1]


def maxValue2(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0: continue
            if i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
    return grid[-1][-1]
