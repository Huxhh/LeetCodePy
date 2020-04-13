# coding=utf-8
# author huxh
# time 2020/4/6 12:17 PM


def twoSum(nums, target):
    if len(nums) == 1:
        return []

    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] == target:
            return [nums[l], nums[r]]
        if nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1
    return []