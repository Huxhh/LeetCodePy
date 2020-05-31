# coding=utf-8
# author huxh
# time 2020/5/9 10:54 AM


def canPermutePalindrome(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] += 1

    cnt = 0
    for k in d:
        if d[k] & 1:
            cnt += 1
    if cnt > 1:
        return False
    return True
