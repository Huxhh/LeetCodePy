# coding=utf-8
# author huxh
# time 2020/4/3 9:08 PM


def singleNumber(nums):
    res = 0
    for i in range(32):
        index = 1 << i
        cnt = 0
        for n in nums:
            if n & index:
                cnt += 1

        if cnt % 3 == 1:
            res |= index
    return res
