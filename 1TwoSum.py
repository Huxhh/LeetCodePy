# -*- coding: utf-8 -*-


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
        d[nums[i]] = i;
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

