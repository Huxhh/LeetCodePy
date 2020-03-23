# coding=utf-8
# author huxh
# time 2020/3/21 10:57 AM

# 动态规划 自顶向下
def cuttingRope(n):
    d = {}

    def back(n):
        if n == 2:
            return 1
        if n in d:
            return d[n]

        res = -1
        for i in range(1, n):
            res = max(res, max(i * (n - i), i * back(n - i)))
        d[n] = res
        return res
    return back(n)

# 动态规划 自底向上
def cuttingRope2(n):
    dp = [0] * (n + 1)

    dp[2] = 1
    for i in range(3, n):
        for j in range(i):
            dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
    return dp[-1]

# 动态规划 优化
def cuttingRope3(n):
    dp = [0, 1, 1]

    for i in range(3, n + 1):
        dp[i % 3] = max(max(dp[(i - 1) % 3], i - 1),
                        2 * max(dp[(i - 2) % 3], i - 2),
                        3 * max(dp[(i - 3) % 3], i - 3))
    return dp[n % 3]

# 找规律
def cuttingRope4(n):
    if n <= 3:
        return n - 1
    a, b = n // 3, n % 3
    if b == 0:
        return pow(3, a)
    if b == 1:
        return pow(3, a - 1) * 4
    return pow(3, a) * 2
