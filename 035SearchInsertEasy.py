# coding=utf-8


"""
思路：
如果插入值大于数组中最大值，直接返回数组长度
否则依次遍历，返回大于插入值的那个值的下标
时间复杂度 O(n) 空间复杂度O(1)
"""


def searchInsert(nums, target):
    if target > nums[-1]:
        return len(nums)
    for i in range(0, len(nums)):
        if nums[i] >= target:
            return i


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 7
    print(searchInsert(nums, target))