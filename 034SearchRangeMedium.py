# coding=utf-8


"""
思路
二分查找找到目标值，从该值下标左右扩散
时间复杂度 O(log n) 空间复杂度 O(1)
"""


def searchRange(nums, target):
    ans = [-1, -1]
    l = 0
    r = len(nums) - 1
    while l <= r:
        middle = (l + r) // 2
        if nums[middle] < target:
            l = middle + 1
        elif nums[middle] > target:
            r = middle - 1
        else:
            tr = middle
            tl = middle
            while tr < len(nums) - 1 and nums[tr + 1] == target:
                tr += 1
            while tl > 0 and nums[tl - 1] == target:
                tl -= 1
            ans[0] = tl
            ans[1] = tr
            break

    return ans


if __name__ == '__main__':
    nums = [1]
    target = 1
    print(searchRange(nums, target))