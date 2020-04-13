# coding=utf-8
# author huxh
# time 2020/4/2 11:02 AM


def search(nums, target):
    if not nums:
        return 0

    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] <= target:
            i = mid + 1
        else:
            j = mid - 1
    right = i

    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] < target:
            i = mid + 1
        else:
            j = mid - 1
    left = j

    return right - left - 1
