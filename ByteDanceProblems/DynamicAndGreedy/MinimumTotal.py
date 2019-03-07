# coding=utf-8


def minimumTotal(triangle):
    n = len(triangle)
    minPath = [triangle[0]]
    for i in range(1, n):
        minPath.append([0] * (i + 1))

    for i in range(1, n):
        for j in range(0, i + 1):
            if j == 0:
                minPath[i][j] = minPath[i - 1][j] + triangle[i][j]
            elif i == j:
                minPath[i][j] = minPath[i - 1][j - 1] + triangle[i][j]
            else:
                minPath[i][j] = min(minPath[i - 1][j - 1] + triangle[i][j], minPath[i - 1][j] + triangle[i][j])

    return min(minPath[-1])


def minimumTotal2(triangle):
    n = len(triangle)
    minPath = triangle[-1]
    for i in range(n - 2, -1, -1):
        for j in range(0, len(triangle[i])):
            minPath[j] = triangle[i][j] + min(minPath[j], minPath[j + 1])

    return minPath[0]
