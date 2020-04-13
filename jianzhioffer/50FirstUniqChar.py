# coding=utf-8
# author huxh
# time 2020/4/2 10:24 AM


def firstUniqChar(s):
    if not s:
        return ' '

    res = {}
    for c in s:
        if c not in res:
            res[c] = 1
        else:
            res[c] += 1
    for c in res:
        if res[c] == 1:
            return c
    return ' '


def firstUniqChar2(s):
    if not s:
        return ' '
    res = {}
    for c in s:
        res[c] = not c in res
    for c in s:
        if res[c]:
            return c
    return ' '
