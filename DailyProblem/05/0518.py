# coding=utf-8
# author huxh
# time 2020/5/18 9:57 AM


def maxProduct(nums):
    mins = [x for x in nums]
    maxs = [x for x in nums]
    for i in range(1, len(nums)):
        maxs[i] = max(mins[i - 1] * nums[i], maxs[i - 1] * nums[i], nums[i])
        mins[i] = min(mins[i - 1] * nums[i], maxs[i - 1] * nums[i], nums[i])
    return max(maxs)


def maxProduct2(nums):
    maxs = nums[0]
    mins = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        mx = maxs
        mn = mins
        maxs = max(mx * nums[i], mn * nums[i], nums[i])
        mins = min(mn * nums[i], mx * nums[i], nums[i])
        res = max(res, maxs)
    return res
