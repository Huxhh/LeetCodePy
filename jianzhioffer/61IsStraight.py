# coding=utf-8
# author huxh
# time 2020/4/7 10:29 AM


def isStraight(nums):
    nums = [num for num in nums if num]
    return len(set(nums)) == len(nums) and max(nums) - min(nums) < 5

