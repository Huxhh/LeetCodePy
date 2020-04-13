# coding=utf-8
# author huxh
# time 2020/4/3 1:44 PM


def singleNumbers(nums):
    bit = 0
    for n in nums:
        bit ^= n

    nbit = 1
    while not nbit & bit:
        nbit <<= 1
    tmp = 0
    for n in nums:
        if nbit & n:
            tmp ^= n
    return [tmp, tmp ^ bit]
