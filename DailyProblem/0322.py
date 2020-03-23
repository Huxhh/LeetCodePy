# coding=utf-8
# author huxh
# time 2020/3/22 9:55 AM

def minIncrementForUnique(A):
    if not A:
        return 0

    res = 0
    d = []
    A = sorted(A)
    arr = [0] * 80000
    for n in A:
        if not arr[n]:
            arr[n] = 1
        else:
            d.append(n)

    for i in range(len(arr)):
        if d and i >= d[0] and arr[i] == 0:
            arr[i] = 1
            res += (i - d[0])
            d.pop(0)

    return res