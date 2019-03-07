# coding=utf-8


def findLengthOfLCIS(nums):
    if not nums:
        return 0

    maxLength = 0
    curLength = 1
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            curLength += 1
        else:
            maxLength = max(maxLength, curLength)
            curLength = 1

    maxLength = max(curLength, maxLength)
    return maxLength

