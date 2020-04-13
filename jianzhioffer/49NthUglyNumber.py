# coding=utf-8
# author huxh
# time 2020/4/2 10:13 AM


def nthUglyNumber(n):
    dp = [0] * n
    dp[0] = 1
    index = 1
    p2, p3, p5 = 0, 0, 0
    while index < n:
        nt = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
        dp[index] = nt
        index += 1
        if nt == dp[p2] * 2:
            p2 += 1
        if nt == dp[p3] * 3:
            p3 += 1
        if nt == dp[p5] * 5:
            p5 += 1
    return dp[n]