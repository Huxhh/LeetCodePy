# coding=utf-8


"""
思路
方法：双指针，nums[index]表示nums[i]前一个数，如果nums[i]不等于nums[index]时，index后移并nums[index = nums[i]，重复此过程
        直到数组结尾 时间复杂度O(n) 空间复杂度O(1)
"""


def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]
    return index + 1


if __name__ == '__main__':
    nums = []
    print(removeDuplicates(nums))
