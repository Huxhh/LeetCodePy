# coding=utf-8
# author huxh
# time 2020/4/1 10:11 AM


def maxDepthAfterSplit(seq):
    ans = []
    d = 0
    for s in seq:
        if s == '(':
            d += 1
            ans.append(d % 2)
        else:
            ans.append(d % 2)
            d -= 1

    return ans


def maxDepthAfterSplit2(seq):
    ans = []
    for i, s in enumerate(seq):
        if s == '(':
            ans.append(i % 2)
        else:
            ans.append(1 - i % 2)
    return ans