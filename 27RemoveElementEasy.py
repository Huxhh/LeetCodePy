# coding=utf-8


"""
思路
方法1：双指针，使用两个指针i,j，如果nums[j]不为val，则复制到nums[i]，直到j到数组末尾，此时数组长度为i
        遍历2n步 时间复杂度O(n) 空间复杂度O(1)
方法2：双指针，当nums[i]等于val时，与最后一个元素交换，此时数组长度为n - 1，循环至i = n
        遍历n步，时间复杂度O(n) 空间复杂度O(1)
"""


def removeElement(nums, val):
    index = len(nums) - 1
    i = 0
    while i <= index:
        while nums[index] == val and index >= 0 and index >= i:
            index -= 1
        if index < 0 or index < i:
            break
        if nums[i] == val:
            tmp = nums[i]
            nums[i] = nums[index]
            nums[index] = tmp
            index -= 1
        i += 1
    return index + 1


def removeElement2(nums, val):
    index = len(nums) - 1
    i = 0
    while i <= index:
        while nums[index] == val and index >= i:
            index -= 1
        if index < i:
            break
        if nums[i] == val:
            tmp = nums[i]
            nums[i] = nums[index]
            nums[index] = tmp
            index -= 1
        i += 1
    return index + 1


def removeELement3(nums, val):
    index = 0
    lens = len(nums)
    for i in range(0, lens):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return index


def removeElement4(nums, val):
    index = len(nums)
    i = 0
    while i < index:
        if nums[i] == val:
            nums[i] = nums[index - 1]
            index -= 1
        else:
            i += 1
    return index


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print(removeElement4(nums, val))
