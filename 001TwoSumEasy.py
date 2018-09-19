# -*- coding: utf-8 -*-


"""
思路
方法1：暴力解法，两两遍历数组当中的数，相加为target时返回，时间复杂度O(n^2) 空间复杂度O(1)
方法2：使用一个map（即dict）结构存储“数值：下标”数据对，这样只需遍历两遍数组，
        查找target-数值在不在dict中，时间复杂度O(n) 空间复杂度O(n)
方法3：只遍历一遍数组，便遍历，便将“数值：下标”数据对加入dict中，找到答案时立刻返回 时间复杂度O(n) 空间复杂O(n)
"""


def twoSum(nums, target):
    lens = len(nums)
    for i in range(0, lens):
        for j in range(i + 1, lens):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum2(nums, target):
    lens = len(nums)
    d = {}
    for i in range(0, lens):
        d[nums[i]] = i
    for i in range(0, lens):
        x = target - nums[i]
        if x in d:
            if d[x] != i:
                return [i, d[x]]


def twoSum3(nums, target):
    lens = len(nums)
    d = {}
    for i in range(0, lens):
        x = target - nums[i]
        if x in d:
            return [d[x], i]
        d[nums[i]] = i


if __name__ == '__main__':
    outnums = [3, 2, 4]
    outtarget = 6
    print(twoSum3(outnums, outtarget))

