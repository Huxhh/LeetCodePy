# coding=utf-8
# author huxh
# time 2020/3/30 5:41 PM


def maxSubArray(nums):
    if not nums:
        return 0

    s = 0
    res = -99999
    for n in nums:
        s += n
        res = max(res, s)
        if s < 0:
            s = 0
    return res


def maxSubArray2(nums):
    res = -99999999
    s = 0
    for n in nums:
        if s < 0:
            s = n
        else:
            s += n
        res = max(res, s)
    return res
