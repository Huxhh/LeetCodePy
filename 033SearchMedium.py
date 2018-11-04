# coding=utf-8


def search(nums, target):
    if not nums:
        return -1
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if i == len(nums) - 1:
            return -1


def search2(nums, target):
    if not nums:
        return -1
    if nums[0] == target:
        return 0
    high = len(nums) - 1
    low = 0
    while low < high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[low] == target:
            return low
        elif nums[high] == target:
            return high
        elif nums[mid] < target:
            low += 1
        elif nums[mid] > target:
            high -= 1

    return -1


def search3(nums, target):
    if not nums:
        return -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1



if __name__ == '__main__':
    nums = [2,1]
    target = 1
    print(search3(nums, target))