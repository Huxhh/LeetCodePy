# coding=utf-8
# author huxh
# time 2020/4/13 3:16 PM


def constructArr(a):
    res = [1] * len(a)

    left = 1
    for i in range(len(a)):
        res[i] = left
        left *= a[i]

    right = 1
    for i in range(len(a) - 1, -1, -1):
        res[i] *= right
        right *= a[i]
    return res
