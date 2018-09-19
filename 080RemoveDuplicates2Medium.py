# coding=utf-8


"""
思路
方法：双指针，index表示移动后的下标，i为原数组下标，同时设立一个标志位flag，当后一位和前一位第一次相等时，
        index后移并复制nums[i]，将flag置0，当第二次相等时，flag为0了，不复制，当后一位与前一位不相等时，
        index后移并复制，循环到数组结束 时间复杂度O(n) 空间复杂度O(1)
"""


def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    index = 0
    flag = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[index]:
            index += 1
            nums[index] = nums[i]
            flag = 1
        elif nums[i] == nums[index] and flag:
            index += 1
            nums[index] = nums[i]
            flag = 0
    return index + 1


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print(removeDuplicates(nums))