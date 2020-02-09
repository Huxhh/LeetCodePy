# coding=utf-8

def sortColors(nums):
    if not nums:
        return nums

    n = len(nums)
    right2 = n - 1
    index = 0
    left0 = 0
    while index <= right2:
        if nums[index] == 0:
            nums[index], nums[left0] = nums[left0], nums[index]
            index += 1
            left0 += 1
        elif nums[index] == 2:
            nums[index], nums[right2] = nums[right2], nums[index]
            right2 -= 1
        else:
            index += 1

    return nums


if __name__ == '__main__':
    nums = [0,1,0]
    print(sortColors(nums))


