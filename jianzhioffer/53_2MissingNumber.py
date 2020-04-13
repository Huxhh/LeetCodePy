# coding=utf-8
# author huxh
# time 2020/4/3 11:53 AM


def missingNumber(nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == m:
            l += 1
        else:
            r -= 1
    return l
