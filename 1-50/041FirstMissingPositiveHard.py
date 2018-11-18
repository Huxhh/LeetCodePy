# coding = utf-8


"""
思路
交换数组元素，使得数组中第i位存放数值(i+1)。最后遍历数组，寻找第一个不符合此要求的元素，返回其下标。整个过程需要遍历两次数组
时间复杂度为 O(n) 空间复杂度 O(1)
"""


def firstMissingPositive(nums):
    for i in range(len(nums)):
        while nums[i] != i + 1 and 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
            temp = nums[i]
            nums[i] = nums[nums[i] - 1]
            nums[temp - 1] = temp

    for i in range(len(nums)):
        if nums[i] != (i + 1):
            return i + 1

    return len(nums) + 1


if __name__ == '__main__':
    nums = [3,4,-1,1]
    print(firstMissingPositive(nums))