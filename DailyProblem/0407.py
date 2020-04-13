# coding=utf-8
# author huxh
# time 2020/4/7 9:27 AM


def rotate(matrix):
    om = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = om[len(matrix) - j - 1][i]


def rotate3(matrix):
    n = len(matrix)

    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
