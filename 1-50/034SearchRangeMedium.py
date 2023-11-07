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


"""
三种二分写法，注意循环不变量
找右边界时可以看做是找大于等于target+1的数，然后最后减1就得到了target的结尾
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def lower_bound2(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def lower_bound3(nums, target):
            left = -1
            right = len(nums)
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            return right

        start = lower_bound(nums, target)
        print(start)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound3(nums, target + 1) - 1
        return [start, end]


if __name__ == '__main__':
    nums = [1]
    target = 1
    print(searchRange(nums, target))