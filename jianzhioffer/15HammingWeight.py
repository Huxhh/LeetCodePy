# coding=utf-8
# author huxh
# time 2020/3/21 11:29 AM


def hammingWeight(n):
    test = 1
    res = 0
    while n:
        if n & test == 1:
            res += 1
        n >>= 1
    return res


def hammingWeight(n):
    res = 0
    while n:
        res += 1
        n &= (n - 1)
    return res