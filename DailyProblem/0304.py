# coding=utf-8

def orangesRotting(grid):
    if not grid:
        return -1

    minutes = 0
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    flag = 1
    while flag:
        flag = 0
        tmp = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    for k in range(len(dx)):
                        x = i + dx[k]
                        y = j + dy[k]
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                            tmp.append((x, y))
                            flag = 1
        for a, b in tmp:
            grid[a][b] = 2
        minutes += 1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return -1

    return minutes - 1

if __name__ == '__main__':
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(orangesRotting(grid))