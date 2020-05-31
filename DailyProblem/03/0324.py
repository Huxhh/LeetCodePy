# coding=utf-8
# author huxh
# time 2020/3/24 10:03 AM


def massage(nums):
    if not nums:
        return 0

    dp = [0] * (len(nums) + 2)
    for i in range(2, len(nums) + 2):
        dp[i] = max(dp[i - 1], nums[i - 2] + dp[i - 2])
    return dp[-1]


def massage2(nums):
    if not nums:
        return 0

    dpi0 = 0
    dpi1 = 0
    for i in range(len(nums)):
        dpi0, dpi1 = dpi1, max(dpi1, nums[i] + dpi0)
    return dpi1