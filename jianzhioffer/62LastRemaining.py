# coding=utf-8
# author huxh
# time 2020/4/13 12:19 PM


def lastRemaining(n, m):
    f = 0
    for i in range(2, n + 1):
        f = (m + f) % i
    return f
