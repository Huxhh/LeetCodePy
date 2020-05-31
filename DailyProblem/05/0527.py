# coding=utf-8
# author huxh
# time 2020/5/27 10:36 AM


def subarraysDivByK(A, K):
    d = {0:1}
    res = 0
    sum = 0
    for a in A:
        sum += a
        tmp = sum % K
        cnt = d.get(tmp, 0)
        res += cnt
        d[tmp] = cnt + 1
    return res
