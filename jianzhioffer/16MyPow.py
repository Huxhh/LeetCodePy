# coding=utf-8
# author huxh
# time 2020/3/23 12:17 PM

# 快速幂 O(logn) O(1)
def myPow(x, n):
    if n == 0:
        return 1
    if n < 0:
        n = -n
        x = 1 / x
    res = 1.0
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res


def myPow2(x, n):
    if n == 0:
        return 1

    if n < 0:
        n = -n
        x = 1 / x

    def back(a, b):
        if b == 0:
            return 1.0
        if b & 1:
            return a * back(a, b - 1)
        else:
            return back(a * a, b // 2)

    return back(x, n)
