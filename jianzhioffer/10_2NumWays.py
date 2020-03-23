# coding=utf-8
# author huxh
# time 2020/3/20 11:59 AM


def numWays(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, a + b
    return b % int(1e9 + 7)