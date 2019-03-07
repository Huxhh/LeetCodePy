# coding=utf-8


def maximalSquare(matrix):
    if not matrix:
        return 0

    maxres = -99999
    rows = len(matrix)
    cols = len(matrix[0])
    dp = []
    for i in range(rows):
        dp.append([0] * cols)

    for i in range(0, cols):
        dp[0][i] = int(matrix[0][i])
        maxres = max(maxres, dp[0][i])

    for i in range(0, rows):
        dp[i][0] = int(matrix[i][0])
        maxres = max(maxres, dp[i][0])

    for i in range(1, rows):
        for j in range(1, cols):
            if int(matrix[i][j]) == 1:
                dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                maxres = max(maxres, dp[i][j])
    return maxres * maxres


if __name__ == '__main__':
    m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(maximalSquare(m))
