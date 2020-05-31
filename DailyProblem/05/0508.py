# coding=utf-8
# author huxh
# time 2020/5/8 10:16 AM


def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    maxside = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == '1':
                maxside = max(1, maxside)

                side = min(rows - i, cols - j)
                for k in range(1, side):
                    flag = True
                    if matrix[i + k][j + k] == '0':
                        break
                    for m in range(k):
                        if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
                            flag = False
                            break
                    if flag:
                        maxside = max(maxside, k + 1)
                    else:
                        break
    return maxside ** 2


def maximalSquare2(matrix):
    if not matrix or not matrix[0]:
        return 0

    maxSide = 0
    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        if matrix[i][0] == '1':
            dp[i][0] = 1
            maxSide = max(maxSide, dp[i][0])

    for i in range(cols):
        if matrix[0][i] == '1':
            dp[0][i] = 1
            maxSide = max(maxSide, dp[0][i])

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                maxSide = max(maxSide, dp[i][j])
    return maxSide ** 2

class Solution:
    def maximalSquare(self, matrix) -> int:
        maxEdge = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i and j:
                    if matrix[i][j]=="1":
                        matrix[i][j]=min(int(matrix[i-1][j-1]),int(matrix[i][j-1]),int(matrix[i-1][j]))+1
                    else:
                        matrix[i][j]=0
                maxEdge = max(maxEdge,int(matrix[i][j]))
        return maxEdge**2
