# coding=utf-8

import math

def findContinuousSequence(target):
    if target == 1:
        return []

    res = []
    limit = target // 2
    for x in range(1, limit + 1):
        tmp = []
        c = 1 - 4 * (x - x * x - 2 * target)
        if c > 0 and -1 + math.sqrt(c) > 0 and -1 + math.sqrt(c) % 2 == 0:
            y = int((math.sqrt(c) - 1) / 2)
            for i in range(x, y + 1):
                tmp.append(i)
            res.append(tmp[:])
    return res


def findContinuousSequence2(target):
    res = []
    l = 1
    r = 2
    while l < r:
        tmp = []
        sum = (l + r) * (r - l + 1) // 2
        if sum == target:
            for k in range(l, r + 1):
                tmp.append(k)
            res.append(tmp[:])
            l += 1
        elif sum < target:
            r += 1
        else:
            l += 1
    return res

if __name__ == '__main__':
    print(findContinuousSequence2(15))