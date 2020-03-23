# coding=utf-8
# author huxh
# time 2020/3/23 4:02 PM


def printNumbers(n):
    import math
    res = []
    for i in range(1, int(math.pow(10, n))):
        res.append(i)
    return res
