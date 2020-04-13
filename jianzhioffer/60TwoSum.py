# coding=utf-8
# author huxh
# time 2020/4/7 10:14 AM

import math
def twoSum(n):
    dp = [[0] * (6 * n + 1) for _ in range(n + 1)]

    for i in range(1, 7):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(i, 6 * i + 1):
            for cur in range(1, 7):
                if j - cur <= 0:
                    break
                dp[i][j] += dp[i - 1][j - cur]

    total = math.pow(6, n)
    res = []
    for i in range(n, 6 * n + 1):
        res.append(dp[n][i] * 1.0 / total)
    return res


def twoSum2(n):
    dp = [0] * (6 * n + 1)
    for i in range(1, 7):
        dp[i] = 1

    for i in range(2, n + 1):
        for j in range(6 * i, i - 1, -1):
            dp[j] = 0
            for cur in range(1, 7):
                if j - cur < i - 1:
                    break
                dp[j] += dp[j - cur]

    total = math.pow(6, n)
    res = []
    for i in range(n, 6 * n + 1):
        res.append(dp[i] * 1.0 / total)
    return res
