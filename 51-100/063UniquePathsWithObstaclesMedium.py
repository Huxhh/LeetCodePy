# coding=utf-8


def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0

    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])

    obstacleGrid[0][0] = 1

    for i in range(1, rows):
        obstacleGrid[i][0] = int(obstacleGrid[i - 1][0] == 1 and obstacleGrid[i][0] == 0)

    for i in range(1, cols):
        obstacleGrid[0][i] = int(obstacleGrid[0][i - 1] == 1 and obstacleGrid[0][i] == 0)

    for i in range(1, rows):
        for j in range(1, cols):
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
            else:
                obstacleGrid[i][j] = 0

    return obstacleGrid[-1][-1]

