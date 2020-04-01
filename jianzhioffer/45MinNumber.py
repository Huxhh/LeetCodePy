# coding=utf-8
# author huxh
# time 2020/3/31 3:30 PM


def minNumber(nums):
    nums = list(map(str, nums))

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] > nums[j] + nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return ''.join(nums)


class cmpSmaller(str):
    def __lt__(self, y):
        return self + y < y + self  # 字符串拼接比较(两两比较)
    # 按由小到大来排列

class Solution:
    def minNumber(self, nums):
        res=sorted(map(str, nums),key=cmpSmaller)
        smallest = ''.join(res)
        return smallest

