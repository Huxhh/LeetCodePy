# coding=utf-8


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